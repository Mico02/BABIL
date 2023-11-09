CFLAGS = -std=c99
LDFLAGS = -I./include/* -L/usr/lib -lvosk -lportaudio
 
audioinfo: audioinfo.c
	g++ audioinfo.c -o audioinfo $(CFLAGS) $(LDFLAGS)


