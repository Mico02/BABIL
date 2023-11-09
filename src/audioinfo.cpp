#include <VoskPackage.h>
#include <portaudio.h>
#include <iostream>
#include <stdlib.h>

int main(void){
    //Intializing portaudio
    if(Pa_Initialize() != paNoError){
        std::cerr << "Error: unable to initialize PortAudio" << std::endl;
        exit(EXIT_FAILURE);
    }

    //List devices
    int deviceCount = Pa_GetDeviceCount();
    const PaDeviceInfo * deviceInfo;
    for(short i = 0; i < deviceCount; i++){
        deviceInfo =  Pa_GetDeviceInfo(i);
        std::cout << "Device name: "  << deviceInfo->name << std::endl;
        std::cout << "Device sample rate: " << deviceInfo->defaultSampleRate << std::endl;
    }

    
}
