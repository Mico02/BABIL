#include "vosk_api.h"
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
class VoskModelClass{
    friend class VoskRecognizerClass;
    private: 
        VoskModel * model;
    public:
    //Constructors and destructors
    VoskModelClass(const char *model_path){
        this->model = vosk_model_new(model_path);
    }
    VoskModelClass(const std::string model_path){
        this->model = vosk_model_new(model_path.c_str());
    }
    ~VoskModelClass(){
        vosk_model_free(this->model);
    }

    //Instance Methods
    void freeModel(){
        vosk_model_free(this->model);
    }

    int findWord(const char * word){
        return vosk_model_find_word(this->model, word);
    }

    int findWord(const std::string word){
        return vosk_model_find_word(this->model, word.c_str());
    }
};
*/
/*
class VoskSPKModelClass{
    friend class VoskRecognizerClass;
    private:
        VoskSpkModel * model;
    public: 
    //Constructors and destructors
    VoskSPKModelClass(const char *model_path){
        this->model = vosk_spk_model_new(model_path);
    }
    VoskSPKModelClass(const std::string model_path){
       this->model = vosk_spk_model_new(model_path.c_str());
    }
    ~VoskSPKModelClass(){
        vosk_spk_model_free(this->model);
    }
    //Instance Methods
    void freeModel(){
        vosk_spk_model_free(this->model);
    }
};
*/
/*
class VoskRecognizerClass{
    private:
        VoskRecognizer * recognizer;
    public:
    //Consructors and destructors
    VoskRecognizerClass(VoskModelClass model, float sampleRate){
        this->recognizer = vosk_recognizer_new(model.model, sampleRate);
    }
    VoskRecognizerClass(VoskModelClass model, VoskSPKModelClass spkModel, float sampleRate){
        this->recognizer = vosk_recognizer_new_spk(model.model, sampleRate, spkModel.model);
    }
    VoskRecognizerClass(VoskModelClass model, float sampleRate, const char * grammar){
        this->recognizer = vosk_recognizer_new_grm(model.model, sampleRate, grammar);
    }
    VoskRecognizerClass(VoskModelClass model, float sampleRate, const std::string grammar){
        this->recognizer = vosk_recognizer_new_grm(model.model, sampleRate, grammar.c_str());
    }
    ~VoskRecognizerClass(){
        vosk_recognizer_free(this->recognizer);
    }

    //Instance Methods
    void setSPKModel(VoskSPKModelClass spkModel){
        vosk_recognizer_set_spk_model(this->recognizer, spkModel.model);
    }

    void setGrammar(const char * grammar){
        vosk_recognizer_set_grm(this->recognizer, grammar);
    }

    void setGrammar(const std::string grammar){
        vosk_recognizer_set_grm(this->recognizer, grammar.c_str());
    }
    
    void setMaxAlternatives(int maxAlternatives){
        vosk_recognizer_set_max_alternatives(this->recognizer, maxAlternatives);
    }

    void setWords(bool words){
        vosk_recognizer_set_words(this->recognizer, (int)words);
    }

    void setPartialWords(bool words){
        vosk_recognizer_set_partial_words(this->recognizer, (int)words);
    }

    void setNLSML(bool nlsml){
        vosk_recognizer_set_nlsml(this->recognizer, (int)nlsml);
    }

    int acceptWaveform(const char * data, int length){
        return vosk_recognizer_accept_waveform(this->recognizer, data, length);
    }

    int acceptWaveformShort(const short * data, int length){
        return vosk_recognizer_accept_waveform_s(this->recognizer, data, length);
    }

    int acceptWaveformFloat(const float * data, int length){
        return vosk_recognizer_accept_waveform_f(this->recognizer, data, length);
    }

    const char * result(){
        return vosk_recognizer_result(this->recognizer);
    }

    const char * partialResult(){
        return vosk_recognizer_partial_result(this->recognizer);
    }

    const char * finalResult(){
        return vosk_recognizer_final_result(this->recognizer);
    }

    void reset(){
        return vosk_recognizer_reset(this->recognizer);
    }
    
};
*/
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