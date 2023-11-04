#include <vosk_api.h>
#include <string>

namespace VoskPackage{

class VoskModelClass{
    friend class VoskRecognizerClass;
    private: 
        VoskModel * model;
    public:
    //Constructors and destructors
    VoskModelClass(const char *model_path);
    VoskModelClass(const std::string model_path);
    ~VoskModelClass();
    
    //Instance Methods
    void freeModel();
    int findWord(const char * word);
    int findWord(const std::string word);
};

class VoskSPKModelClass{
    friend class VoskRecognizerClass;
    private:
        VoskSpkModel * model;
    public: 
    //Constructors and destructors
    VoskSPKModelClass(const char *model_path);
    VoskSPKModelClass(const std::string model_path);
    ~VoskSPKModelClass();
    //Instance Methods
    void freeModel();
};

class VoskRecognizerClass{
    private:
        VoskRecognizer * recognizer;
    public:
    //Consructors and destructors
    VoskRecognizerClass(VoskModelClass model, float sampleRate);
    VoskRecognizerClass(VoskModelClass model, VoskSPKModelClass spkModel, float sampleRate);
    VoskRecognizerClass(VoskModelClass model, float sampleRate, const char * grammar);
    VoskRecognizerClass(VoskModelClass model, float sampleRate, const std::string grammar);
    ~VoskRecognizerClass();

    //Instance Methods
    void setSPKModel(VoskSPKModelClass spkModel);
    void setGrammar(const char * grammar);
    void setGrammar(const std::string grammar);
    void setMaxAlternatives(int maxAlternatives);
    void setWords(bool words);
    void setPartialWords(bool words);
    void setNLSML(bool nlsml);
    int acceptWaveform(const char * data, int length);
    int acceptWaveformShort(const short * data, int length);
    int acceptWaveformFloat(const float * data, int length);
    const char * result();
    const char * partialResult();
    const char * finalResult();
    void reset();
    
};

class VoskBatchModelClass{
    friend class VoskBatchRecognizerClass;
    private:
        VoskBatchModel * batchModel;
    public:
    VoskBatchModelClass(const char * model_path);
    VoskBatchModelClass(std::string model_path);
    ~VoskBatchModelClass();
    //Instance methods
    void wait(){
        vosk_batch_model_wait(this->batchModel);
    }    
};

class VoskBatchRecognizerClass{
    private:
    VoskBatchRecognizer * batchRecognizer;
    public:
    VoskBatchRecognizerClass(VoskBatchModelClass batchRecognizer, float sampleRate);
    ~VoskBatchRecognizerClass();

    //Instance methods
    void acceptWaveform(const char * data, int length);
    void setNLSML(bool nlsml);
    void finishStream();
    void frontResult();
    void pop();
};

}

/*
class VoskBatchModelClass{
    friend class VoskBatchRecognizerClass;
    private:
        VoskBatchModel * batchModel;
    public:
    VoskBatchModelClass(const char * model_path){
        vosk_batch_model_new(model_path);
    }
    VoskBatchModelClass(std::string model_path){
        vosk_batch_model_new(model_path.c_str());
    }
    ~VoskBatchModelClass(){
        vosk_batch_model_free(this->batchModel);
    }
    //Instance methods
    void wait(){
        vosk_batch_model_wait(this->batchModel);
    }    
};
*/
/*
class VoskBatchRecognizerClass{
    private:
    VoskBatchRecognizer * batchRecognizer;
    public:
    VoskBatchRecognizerClass(VoskBatchModelClass batchRecognizer, float sampleRate){
        vosk_batch_recognizer_new(batchRecognizer.batchModel, sampleRate);
    }
    ~VoskBatchRecognizerClass(){
        vosk_batch_recognizer_free(this->batchRecognizer);
    }

    //Instance methods
    void acceptWaveform(const char * data, int length){
        vosk_batch_recognizer_accept_waveform(this->batchRecognizer,data, length);
    }

    void setNLSML(bool nlsml){
        vosk_batch_recognizer_set_nlsml(this->batchRecognizer, (int)nlsml);
    }

    void finishStream(){
        vosk_batch_recognizer_finish_stream(this->batchRecognizer);
    }

    void frontResult(){
        vosk_batch_recognizer_front_result(this->batchRecognizer);
    }

    void pop(){
        vosk_batch_recognizer_pop(this->batchRecognizer);
    }
};
*/