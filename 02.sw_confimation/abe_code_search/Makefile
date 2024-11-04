CFLAGS=-Wall
RELIC_ROOT = ../lib

OPT_INC = -std=gnu99 -I ${RELIC_ROOT}/relic-main/include -I ${RELIC_ROOT}/relic-target/include -I $(CURDIR)

all: abe_time abe_util abe_core abe_highlib main
	gcc ${CFLAGS} -o main main.o abe_time.o abe_util.o abe_core.o abe_highlib.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a

h1: h1_1setup h1_2editatt h1_3user_regis h1_4encrypt h1_5decrypt
	gcc ${CFLAGS} -o $(CURDIR)/chk/h1_1setup h1_1setup.o abe_time.o abe_util.o abe_core.o abe_highlib.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a
	gcc ${CFLAGS} -o $(CURDIR)/chk/h1_2editatt h1_2editatt.o abe_time.o abe_util.o abe_core.o abe_highlib.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a
	gcc ${CFLAGS} -o $(CURDIR)/chk/h1_3user_regis h1_3user_regis.o abe_time.o abe_util.o abe_core.o abe_highlib.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a
	gcc ${CFLAGS} -o $(CURDIR)/chk/h1_4encrypt h1_4encrypt.o abe_time.o abe_util.o abe_core.o abe_highlib.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a
	gcc ${CFLAGS} -o $(CURDIR)/chk/h1_5decrypt h1_5decrypt.o abe_time.o abe_util.o abe_core.o abe_highlib.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a

h2: h2_1setup h2_3user_regis h2_4encrypt h2_5decrypt
	gcc ${CFLAGS} -o $(CURDIR)/chk2/h2_1setup h2_1setup.o abe_time.o abe_util.o abe_core.o abe_highlib.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a
	gcc ${CFLAGS} -o $(CURDIR)/chk2/h2_3user_regis h2_3user_regis.o abe_time.o abe_util.o abe_core.o abe_highlib.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a
	gcc ${CFLAGS} -o $(CURDIR)/chk2/h2_4encrypt h2_4encrypt.o abe_time.o abe_util.o abe_core.o abe_highlib.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a
	gcc ${CFLAGS} -o $(CURDIR)/chk2/h2_5decrypt h2_5decrypt.o abe_time.o abe_util.o abe_core.o abe_highlib.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a

abe_time: abe_time.c
	gcc ${CFLAGS} -c abe_time.c -o abe_time.o $(OPT_INC)

abe_util: abe_util.c
	gcc ${CFLAGS} -c abe_util.c -o abe_util.o $(OPT_INC)

abe_core: abe_core.c
	gcc ${CFLAGS} -c abe_core.c -o abe_core.o $(OPT_INC)

abe_highlib: abe_highlib.c
	gcc ${CFLAGS} -c abe_highlib.c -o abe_highlib.o $(OPT_INC)

main: main.c
	gcc ${CFLAGS} -c main.c -o main.o $(OPT_INC)

h1_1setup: h1_1setup.c
	gcc ${CFLAGS} -c h1_1setup.c -o h1_1setup.o $(OPT_INC)

h1_2editatt: h1_2editatt.c
	gcc ${CFLAGS} -c h1_2editatt.c -o h1_2editatt.o $(OPT_INC)

h1_3user_regis: h1_3user_regis.c
	gcc ${CFLAGS} -c h1_3user_regis.c -o h1_3user_regis.o $(OPT_INC)

h1_4encrypt: h1_4encrypt.c
	gcc ${CFLAGS} -c h1_4encrypt.c -o h1_4encrypt.o $(OPT_INC)

h1_5decrypt: h1_5decrypt.c
	gcc ${CFLAGS} -c h1_5decrypt.c -o h1_5decrypt.o $(OPT_INC)

h2_1setup: h2_1setup.c
	gcc ${CFLAGS} -c h2_1setup.c -o h2_1setup.o $(OPT_INC)

h2_3user_regis: h2_3user_regis.c
	gcc ${CFLAGS} -c h2_3user_regis.c -o h2_3user_regis.o $(OPT_INC)

h2_4encrypt: h2_4encrypt.c
	gcc ${CFLAGS} -c h2_4encrypt.c -o h2_4encrypt.o $(OPT_INC)

h2_5decrypt: h2_5decrypt.c
	gcc ${CFLAGS} -c h2_5decrypt.c -o h2_5decrypt.o $(OPT_INC)

clean:
	rm -rf *.o main
