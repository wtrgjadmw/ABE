`timescale 1ns / 1ps

`include "header_core.vh"

module abe_core_alu(clk,rst,operate,INST1,ALU_din_en,ALU_din,ALU_dout);
    parameter DAT_BITS = 381;
    input wire clk;
    input wire rst;
    input wire operate; // Should be use to stop the usage when not used
    input wire [`ALU_INST_BITS-1:0] INST1;
    input wire ALU_din_en;
    input wire [DAT_BITS-1:0] ALU_din;
    output wire [DAT_BITS-1:0] ALU_dout;

    reg [DAT_BITS-1:0] ALU_din_reg;
    wire ALU_din_en_pipe;
    always @ (posedge clk) begin
        ALU_din_reg <= ALU_din;
    end
    pipe #( .DAT_BITS(1),.PIPE_STG(2),.FORCE_FF("false") )
            pipe_din_en ( .clk(clk),.rst(rst),.din(ALU_din_en),.dout(ALU_din_en_pipe) );


    // MAIN Memory and its relevant signals
    wire [`INST_MAIN_MEM_MUX_BIT-1: 0] Main_MEM_MUX; 
    wire MAIN_MEM_we;
    wire [DAT_BITS-1:0] MAIN_MEM_douta,MAIN_MEM_doutb,MAIN_MEM_din;
    wire [`ALU_MAIN_MEM_ADDR_BITS-1:0] MAIN_MEM_raddra,MAIN_MEM_raddrb,MAIN_MEM_waddr;

    assign MAIN_MEM_waddr = INST2[`INDEX_MAIN_WRITE +: `ALU_MAIN_MEM_ADDR_BITS];
    assign MAIN_MEM_raddra = INST1[`INDEX_MAIN_READA +: `ALU_MAIN_MEM_ADDR_BITS];
    assign MAIN_MEM_raddrb = INST1[`INDEX_MAIN_READB +: `ALU_MAIN_MEM_ADDR_BITS];
    assign MAIN_MEM_we = INST2[`INDEX_MAIN_WE];
    assign Main_MEM_MUX = INST2[`INDEX_MAIN_WRITE_MUX +: `INST_MAIN_MEM_MUX_BIT];

    ram2r1w_tdpram #( .DAT_BITS(DAT_BITS), .MEM_SIZE(`ALU_MAIN_MEM_SIZE), .ADDR_BITS(`ALU_MAIN_MEM_ADDR_BITS),.READ_LAT(1),.INIT_FILE("RAMINIT_ALU_MAIN_MEM.mem") ) 
                    MAIN_MEM( .clk(clk),.rst(rst),.douta(MAIN_MEM_douta),.doutb(MAIN_MEM_doutb),.raddra(MAIN_MEM_raddra),.raddrb(MAIN_MEM_raddrb),.din(MAIN_MEM_din),.waddr(MAIN_MEM_waddr),.we(MAIN_MEM_we));

    // Read out
    reg [DAT_BITS-1:0] ALU_dout_REG;
    assign ALU_dout = ALU_dout_REG;
    always @ (posedge clk) begin
        if (rst) begin
            ALU_dout_REG <= 'b0;
        end else begin
            ALU_dout_REG <= MAIN_MEM_doutb;
        end
    end

	// CAL_MUX_MODE
	localparam mux_MM0_MEM = `INST_CAL_MUX_BIT'd0;
	localparam mux_MM0_SC = `INST_CAL_MUX_BIT'd1;
	localparam mux_MM0_REG = `INST_CAL_MUX_BIT'd2;
	localparam mux_MAS0_MEM = `INST_CAL_MUX_BIT'd3;
	localparam mux_MAS0_SC = `INST_CAL_MUX_BIT'd4;
	localparam mux_MAS0_REG = `INST_CAL_MUX_BIT'd5;
	localparam mux_MAS1_MEM = `INST_CAL_MUX_BIT'd6;
	localparam mux_MAS1_SC = `INST_CAL_MUX_BIT'd7;
	localparam mux_MAS1_REG = `INST_CAL_MUX_BIT'd8;
	localparam mux_MAIN_MEM = `INST_CAL_MUX_BIT'd9;


	// MAIN_MEM_INPUT_MODE
	localparam mux_MAIN_MM0 = `INST_MAIN_MEM_MUX_BIT'd0;
	localparam mux_MAIN_MAS0 = `INST_MAIN_MEM_MUX_BIT'd1;
	localparam mux_MAIN_MAS1 = `INST_MAIN_MEM_MUX_BIT'd2;
	assign MAIN_MEM_din = ALU_din_en_pipe == 1'b1 ? ALU_din_reg
			: (Main_MEM_MUX == mux_MAIN_MM0 ? MM0_dout
			: (Main_MEM_MUX == mux_MAIN_MAS0 ? MAS0_dout
			: (Main_MEM_MUX == mux_MAIN_MAS1 ? MAS1_dout
			: 0 )));
    // MM0 (Modular Multiplication) Memory and its relevant signals
    wire MM0_MEM_we;
    wire [DAT_BITS-1:0] MM0_MEM_douta,MM0_MEM_doutb,MM0_MEM_din;
    wire [`ALU_MM_MEM_ADDR_BITS-1:0] MM0_MEM_raddra,MM0_MEM_raddrb,MM0_MEM_waddr;

    ram2r1w_tdpram #( .DAT_BITS(DAT_BITS), .MEM_SIZE(`ALU_MM_MEM_SIZE), .ADDR_BITS(`ALU_MM_MEM_ADDR_BITS),.READ_LAT(1),.INIT_FILE("RAMINIT_ALU_MM0_MEM.mem") ) 
                    MM0_MEM ( .clk(clk),.rst(rst),.douta(MM0_MEM_douta),.doutb(MM0_MEM_doutb),.raddra(MM0_MEM_raddra),.raddrb(MM0_MEM_raddrb),.din(MM0_MEM_din),.waddr(MM0_MEM_waddr),.we(MM0_MEM_we));
    wire [DAT_BITS-1:0] MM0_dina,MM0_dinb,MM0_dout;
    reg [DAT_BITS-1:0] MM0_dout_reg;
    wire MM0_ival,MM0_oval;
    wire MM0_retin_wea,MM0_retout_we;
    wire [`ALU_MM_MEM_ADDR_BITS-1:0] MM0_retin_waddra,MM0_retout_waddr;
    wire [`INST_CAL_MUX_BIT-1:0] MM0_muxa,MM0_muxb;

    assign MM0_MEM_raddra = INST1[`INDEX_MM0_READA +: `ALU_MM_MEM_ADDR_BITS];
    assign MM0_muxa = INST2[`INDEX_MM0_MUXA +: `INST_CAL_MUX_BIT];
    assign MM0_MEM_raddrb = INST1[`INDEX_MM0_READB +: `ALU_MM_MEM_ADDR_BITS];
    assign MM0_muxb = INST2[`INDEX_MM0_MUXB +: `INST_CAL_MUX_BIT];
    assign MM0_MEM_waddr = MM0_retout_waddr;
    assign MM0_MEM_we = MM0_retout_we;
    assign MM0_MEM_din = MM0_dout ;
    assign MM0_ival = INST2[`INDEX_MM0_VAL];
    assign MM0_retin_waddra = INST2[`INDEX_MM0_WRITE +: `ALU_MM_MEM_ADDR_BITS];
    assign MM0_retin_wea = INST2[`INDEX_MM0_WE];

    mm_wrap #(.BIT_LEN(DAT_BITS)) mm0_wrap ( .clk(clk),.rst(rst),.dina(MM0_dina),.dinb(MM0_dinb),.retaddr_in({MM0_retin_wea,MM0_retin_waddra}),
                                            .dout(MM0_dout),.retaddr_out({MM0_retout_we,MM0_retout_waddr}),.ival(MM0_ival),.oval(MM0_oval) );
	assign MM0_dina = 
					MM0_muxa == mux_MM0_MEM ? MM0_MEM_douta
					 : (MM0_muxa == mux_MM0_SC ? MM0_dout
					 : (MM0_muxa == mux_MM0_REG ? MM0_dout_reg
					 : (MM0_muxa == mux_MAS0_MEM ? MAS0_MEM_douta
					 : (MM0_muxa == mux_MAS0_SC ? MAS0_dout
					 : (MM0_muxa == mux_MAS0_REG ? MAS0_dout_reg
					 : (MM0_muxa == mux_MAS1_MEM ? MAS1_MEM_douta
					 : (MM0_muxa == mux_MAS1_SC ? MAS1_dout
					 : (MM0_muxa == mux_MAS1_REG ? MAS1_dout_reg
					: MAIN_MEM_douta ))))))));

	assign MM0_dinb = 
					MM0_muxb == mux_MM0_MEM ? MM0_MEM_doutb
					 : (MM0_muxb == mux_MM0_SC ? MM0_dout
					 : (MM0_muxb == mux_MM0_REG ? MM0_dout_reg
					 : (MM0_muxb == mux_MAS0_MEM ? MAS0_MEM_doutb
					 : (MM0_muxb == mux_MAS0_SC ? MAS0_dout
					 : (MM0_muxb == mux_MAS0_REG ? MAS0_dout_reg
					 : (MM0_muxb == mux_MAS1_MEM ? MAS1_MEM_doutb
					 : (MM0_muxb == mux_MAS1_SC ? MAS1_dout
					 : (MM0_muxb == mux_MAS1_REG ? MAS1_dout_reg
					: MAIN_MEM_doutb ))))))));

    // MAS0 (Modular Adder/Subtractor) Memory and its relevant signals
    wire MAS0_MEM_we;
    wire [DAT_BITS-1:0] MAS0_MEM_douta,MAS0_MEM_doutb,MAS0_MEM_din;
    wire [`ALU_MAS_MEM_ADDR_BITS-1:0] MAS0_MEM_raddra,MAS0_MEM_raddrb,MAS0_MEM_waddr;
    ram2r1w_tdpram #( .DAT_BITS(DAT_BITS), .MEM_SIZE(`ALU_MAS_MEM_SIZE), .ADDR_BITS(`ALU_MAS_MEM_ADDR_BITS),.READ_LAT(1),.INIT_FILE("RAMINIT_ALU_MAS0_MEM.mem") ) 
                    MAS0_MEM( .clk(clk),.rst(rst),.douta(MAS0_MEM_douta),.doutb(MAS0_MEM_doutb),.raddra(MAS0_MEM_raddra),.raddrb(MAS0_MEM_raddrb),.din(MAS0_MEM_din),.waddr(MAS0_MEM_waddr),.we(MAS0_MEM_we));
    wire [DAT_BITS-1:0] MAS0_dina,MAS0_dinb,MAS0_dout;
    reg [DAT_BITS-1:0] MAS0_dout_reg;
    wire MAS0_ival,MAS0_oval;
    wire issub0;
    wire MAS0_retin_web,MAS0_retout_we;
    wire [`ALU_MAS_MEM_ADDR_BITS-1:0] MAS0_retin_waddrb,MAS0_retout_waddr;
    wire [`INST_CAL_MUX_BIT-1:0] MAS0_muxa,MAS0_muxb;

    assign MAS0_MEM_raddra = INST1[`INDEX_MAS0_READA +: `ALU_MAS_MEM_ADDR_BITS];
    assign MAS0_muxa = INST2[`INDEX_MAS0_MUXA +: `INST_CAL_MUX_BIT];
    assign MAS0_MEM_raddrb = INST1[`INDEX_MAS0_READB +: `ALU_MAS_MEM_ADDR_BITS];
    assign MAS0_muxb = INST2[`INDEX_MAS0_MUXB +: `INST_CAL_MUX_BIT];
    assign MAS0_MEM_waddr = MAS0_retout_waddr;
    assign MAS0_MEM_we = MAS0_retout_we;
    assign MAS0_MEM_din = MAS0_dout ;
    assign MAS0_ival = INST2[`INDEX_MAS0_VAL];
    assign issub0 = INST2[`INDEX_MAS0_ISSUB];
    assign MAS0_retin_waddrb = INST2[`INDEX_MAS0_WRITE +: `ALU_MAS_MEM_ADDR_BITS];
    assign MAS0_retin_web = INST2[`INDEX_MAS0_WE];

    mas_wrap #(.BIT_LEN(DAT_BITS)) mas0_wrap (.clk(clk),.rst(rst), .issub(issub0), .dina(MAS0_dina),.dinb(MAS0_dinb),.retaddr_in({MAS0_retin_web,MAS0_retin_waddrb}),
                                            .dout(MAS0_dout),.retaddr_out({MAS0_retout_we,MAS0_retout_waddr}),.ival(MAS0_ival),.oval(MAS0_oval));
	assign MAS0_dina = 
					MAS0_muxa == mux_MM0_MEM ? MM0_MEM_douta
					 : (MAS0_muxa == mux_MM0_SC ? MM0_dout
					 : (MAS0_muxa == mux_MM0_REG ? MM0_dout_reg
					 : (MAS0_muxa == mux_MAS0_MEM ? MAS0_MEM_douta
					 : (MAS0_muxa == mux_MAS0_SC ? MAS0_dout
					 : (MAS0_muxa == mux_MAS0_REG ? MAS0_dout_reg
					 : (MAS0_muxa == mux_MAS1_MEM ? MAS1_MEM_douta
					 : (MAS0_muxa == mux_MAS1_SC ? MAS1_dout
					 : (MAS0_muxa == mux_MAS1_REG ? MAS1_dout_reg
					: MAIN_MEM_douta ))))))));

	assign MAS0_dinb = 
					MAS0_muxb == mux_MM0_MEM ? MM0_MEM_doutb
					 : (MAS0_muxb == mux_MM0_SC ? MM0_dout
					 : (MAS0_muxb == mux_MM0_REG ? MM0_dout_reg
					 : (MAS0_muxb == mux_MAS0_MEM ? MAS0_MEM_doutb
					 : (MAS0_muxb == mux_MAS0_SC ? MAS0_dout
					 : (MAS0_muxb == mux_MAS0_REG ? MAS0_dout_reg
					 : (MAS0_muxb == mux_MAS1_MEM ? MAS1_MEM_doutb
					 : (MAS0_muxb == mux_MAS1_SC ? MAS1_dout
					 : (MAS0_muxb == mux_MAS1_REG ? MAS1_dout_reg
					: MAIN_MEM_doutb ))))))));

    // MAS1 (Modular Adder/Subtractor) Memory and its relevant signals
    wire MAS1_MEM_we;
    wire [DAT_BITS-1:0] MAS1_MEM_douta,MAS1_MEM_doutb,MAS1_MEM_din;
    wire [`ALU_MAS_MEM_ADDR_BITS-1:0] MAS1_MEM_raddra,MAS1_MEM_raddrb,MAS1_MEM_waddr;
    ram2r1w_tdpram #( .DAT_BITS(DAT_BITS), .MEM_SIZE(`ALU_MAS_MEM_SIZE), .ADDR_BITS(`ALU_MAS_MEM_ADDR_BITS),.READ_LAT(1),.INIT_FILE("RAMINIT_ALU_MAS1_MEM.mem") ) 
                    MAS1_MEM( .clk(clk),.rst(rst),.douta(MAS1_MEM_douta),.doutb(MAS1_MEM_doutb),.raddra(MAS1_MEM_raddra),.raddrb(MAS1_MEM_raddrb),.din(MAS1_MEM_din),.waddr(MAS1_MEM_waddr),.we(MAS1_MEM_we));
    wire [DAT_BITS-1:0] MAS1_dina,MAS1_dinb,MAS1_dout;
    reg [DAT_BITS-1:0] MAS1_dout_reg;
    wire MAS1_ival,MAS1_oval;
    wire issub1;
    wire MAS1_retin_web,MAS1_retout_we;
    wire [`ALU_MAS_MEM_ADDR_BITS-1:0] MAS1_retin_waddrb,MAS1_retout_waddr;
    wire [`INST_CAL_MUX_BIT-1:0] MAS1_muxa,MAS1_muxb;

    assign MAS1_MEM_raddra = INST1[`INDEX_MAS1_READA +: `ALU_MAS_MEM_ADDR_BITS];
    assign MAS1_muxa = INST2[`INDEX_MAS1_MUXA +: `INST_CAL_MUX_BIT];
    assign MAS1_MEM_raddrb = INST1[`INDEX_MAS1_READB +: `ALU_MAS_MEM_ADDR_BITS];
    assign MAS1_muxb = INST2[`INDEX_MAS1_MUXB +: `INST_CAL_MUX_BIT];
    assign MAS1_MEM_waddr = MAS1_retout_waddr;
    assign MAS1_MEM_we = MAS1_retout_we;
    assign MAS1_MEM_din = MAS1_dout ;
    assign MAS1_ival = INST2[`INDEX_MAS1_VAL];
    assign issub1 = INST2[`INDEX_MAS1_ISSUB];
    assign MAS1_retin_waddrb = INST2[`INDEX_MAS1_WRITE +: `ALU_MAS_MEM_ADDR_BITS];
    assign MAS1_retin_web = INST2[`INDEX_MAS1_WE];

    mas_wrap #(.BIT_LEN(DAT_BITS)) mas1_wrap (.clk(clk),.rst(rst), .issub(issub1), .dina(MAS1_dina),.dinb(MAS1_dinb),.retaddr_in({MAS1_retin_web,MAS1_retin_waddrb}),
                                            .dout(MAS1_dout),.retaddr_out({MAS1_retout_we,MAS1_retout_waddr}),.ival(MAS1_ival),.oval(MAS1_oval));
	assign MAS1_dina = 
					MAS1_muxa == mux_MM0_MEM ? MM0_MEM_douta
					 : (MAS1_muxa == mux_MM0_SC ? MM0_dout
					 : (MAS1_muxa == mux_MM0_REG ? MM0_dout_reg
					 : (MAS1_muxa == mux_MAS0_MEM ? MAS0_MEM_douta
					 : (MAS1_muxa == mux_MAS0_SC ? MAS0_dout
					 : (MAS1_muxa == mux_MAS0_REG ? MAS0_dout_reg
					 : (MAS1_muxa == mux_MAS1_MEM ? MAS1_MEM_douta
					 : (MAS1_muxa == mux_MAS1_SC ? MAS1_dout
					 : (MAS1_muxa == mux_MAS1_REG ? MAS1_dout_reg
					: MAIN_MEM_douta ))))))));

	assign MAS1_dinb = 
					MAS1_muxb == mux_MM0_MEM ? MM0_MEM_doutb
					 : (MAS1_muxb == mux_MM0_SC ? MM0_dout
					 : (MAS1_muxb == mux_MM0_REG ? MM0_dout_reg
					 : (MAS1_muxb == mux_MAS0_MEM ? MAS0_MEM_doutb
					 : (MAS1_muxb == mux_MAS0_SC ? MAS0_dout
					 : (MAS1_muxb == mux_MAS0_REG ? MAS0_dout_reg
					 : (MAS1_muxb == mux_MAS1_MEM ? MAS1_MEM_doutb
					 : (MAS1_muxb == mux_MAS1_SC ? MAS1_dout
					 : (MAS1_muxb == mux_MAS1_REG ? MAS1_dout_reg
					: MAIN_MEM_doutb ))))))));

	// Instructions assignment
	reg [`ALU_INST_BITS-1:0] INST2;
	always @ (posedge clk or posedge rst) begin
		if (rst) begin
			INST2 <= 'b0;
			MM0_dout_reg <= 'b0;
			MAS0_dout_reg <= 'b0;
			MAS1_dout_reg <= 'b0;
		end else begin
			INST2 <= INST1;
			MM0_dout_reg <= MM0_dout;
			MAS0_dout_reg <= MAS0_dout;
			MAS1_dout_reg <= MAS1_dout;
		end
	end

endmodule
