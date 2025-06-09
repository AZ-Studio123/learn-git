CC = gcc
CFLAGS = -Iinclude -Wall -Wextra
LIB_NAME = libmathutils.a

OBJ = src/math_utils.o

all: $(LIB_NAME) main

$(LIB_NAME): $(OBJ)
	ar rcs $(LIB_NAME) $(OBJ)

main: main.c $(LIB_NAME)
	$(CC) $(CFLAGS) -o main main.c -L. -lmathutils

src/math_utils.o: src/math_utils.c include/math_utils.h
	$(CC) $(CFLAGS) -c src/math_utils.c -o src/math_utils.o

clean:
	rm -f main $(LIB_NAME) src/*.o
