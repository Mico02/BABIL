LDFLAGS = -I./include/* -L/usr/lib -lvosk -lportaudio
 
audioinfo: src/audioinfo.cpp
	g++ ./src/audioinfo.cpp -o audioinfo $(CFLAGS) $(LDFLAGS)



