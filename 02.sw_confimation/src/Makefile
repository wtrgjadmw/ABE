CFLAGS=-Wall
RELIC_ROOT = ../lib

OPT_INC = -std=gnu99 -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE -D_LARGE_FILE_SOURCE -I ${RELIC_ROOT}/relic-main/include -I ${RELIC_ROOT}/relic-target/include -I $(CURDIR)

all:
	gcc ${CFLAGS} -c main.c -o main.o $(OPT_INC)
	gcc ${CFLAGS} -o main main.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a

t:
	gcc ${CFLAGS} -c tt.c -o tt.o $(OPT_INC)
	gcc ${CFLAGS} -o tt tt.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a

h:
	gcc ${CFLAGS} -c hash.c -o hash.o $(OPT_INC)
	gcc ${CFLAGS} -o hash hash.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a

o:
	gcc ${CFLAGS} -c oate.c -o oate.o $(OPT_INC)
	gcc ${CFLAGS} -o oate oate.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a

m:
	gcc ${CFLAGS} -c mul2.c -o mul2.o $(OPT_INC)
	gcc ${CFLAGS} -o mul2 mul2.o ${RELIC_ROOT}/relic-target/lib/librelic_s.a

clean:
	rm -rf *.o main
