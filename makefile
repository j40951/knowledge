#!/usr/bin/env make -f

CC = g++
CFLAGS  := -g -D_SUSE_LINUX -Wunused-function -std=c++11

INC_ROOT = ./
LIB_ROOT = ../../lib/release/

LIB = $(LIB_ROOT)/libsqltrace_model.so

INC= -I$(INC_ROOT) -I$(U2K_VOB_ROOT)/bizplane/biz_frame/code/server/include -I../../../xReflection/include

INCLUDE_PATH = $(INC)

LIB_PATH = -L $(LIB_ROOT) -L$(U2K_CPP_SDK_ROOT)/biz_frame/server/lib/$(BUILD_TYPE)

DEPEND_LIBS = -lxreflection -lstdc++

all : $(LIB)

SOURCES = $(wildcard *.c *.cpp)
OBJS = $(patsubst %.c,%.o,$(patsubst %.cpp,%.o,$(SOURCES)))
HEADERS := $(shell find . -name "*.h")

%.o : %.cpp $(HEADERS)
	$(CC) $(CFLAGS) -fpic -c $< -o $@ ${INCLUDE_PATH}

$(LIB) : $(OBJS)
	g++ -shared -Wl,-z,defs -o $@ $(OBJS) ${LIB_PATH} ${DEPEND_LIBS}

clean:
	rm -f $(OBJS) $(LIB)
