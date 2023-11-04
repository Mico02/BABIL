#include <VoskPackage.h>
using namespace VoskPackage;

// VoskModelClass Implementations

VoskModelClass::VoskModelClass(const char *model_path){
    this->model = vosk_model_new(model_path);
}

VoskModelClass::VoskModelClass(const std::string model_path){
    this->model = vosk_model_new(model_path.c_str());
}

VoskModelClass::~VoskModelClass(){
    vosk_model_free(this->model);
}

//Instance Methods
void VoskModelClass::freeModel(){
    vosk_model_free(this->model);
}

int VoskModelClass::findWord(const char * word){
    return vosk_model_find_word(this->model, word);
}

int VoskModelClass::findWord(const std::string word){
    return vosk_model_find_word(this->model, word.c_str());
}

//VoskSPKModelClass Implementations
VoskSPKModelClass::VoskSPKModelClass(const char *model_path){
    this->model = vosk_spk_model_new(model_path);
}
VoskSPKModelClass::VoskSPKModelClass(const std::string model_path){
    this->model = vosk_spk_model_new(model_path.c_str());
}
VoskSPKModelClass::~VoskSPKModelClass(){
    vosk_spk_model_free(this->model);
}
//Instance Methods
void VoskSPKModelClass::freeModel(){
    vosk_spk_model_free(this->model);
}

//VoskRecognizerClass Implementations

//Consructors and destructors
VoskRecognizerClass::VoskRecognizerClass(VoskModelClass model, float sampleRate){
    this->recognizer = vosk_recognizer_new(model.model, sampleRate);
}
VoskRecognizerClass::VoskRecognizerClass(VoskModelClass model, VoskSPKModelClass spkModel, float sampleRate){
    this->recognizer = vosk_recognizer_new_spk(model.model, sampleRate, spkModel.model);
}
VoskRecognizerClass::VoskRecognizerClass(VoskModelClass model, float sampleRate, const char * grammar){
    this->recognizer = vosk_recognizer_new_grm(model.model, sampleRate, grammar);
}
VoskRecognizerClass::VoskRecognizerClass(VoskModelClass model, float sampleRate, const std::string grammar){
    this->recognizer = vosk_recognizer_new_grm(model.model, sampleRate, grammar.c_str());
}
VoskRecognizerClass::~VoskRecognizerClass(){
    vosk_recognizer_free(this->recognizer);
}
//Instance Methods
void VoskRecognizerClass::setSPKModel(VoskSPKModelClass spkModel){
    vosk_recognizer_set_spk_model(this->recognizer, spkModel.model);
}
void VoskRecognizerClass::setGrammar(const char * grammar){
    vosk_recognizer_set_grm(this->recognizer, grammar);
}
void VoskRecognizerClass::setGrammar(const std::string grammar){
    vosk_recognizer_set_grm(this->recognizer, grammar.c_str());
}

void VoskRecognizerClass::setMaxAlternatives(int maxAlternatives){
    vosk_recognizer_set_max_alternatives(this->recognizer, maxAlternatives);
}
void VoskRecognizerClass::setWords(bool words){
    vosk_recognizer_set_words(this->recognizer, (int)words);
}
void VoskRecognizerClass::setPartialWords(bool words){
    vosk_recognizer_set_partial_words(this->recognizer, (int)words);
}
void VoskRecognizerClass::setNLSML(bool nlsml){
    vosk_recognizer_set_nlsml(this->recognizer, (int)nlsml);
}
int VoskRecognizerClass::acceptWaveform(const char * data, int length){
    return vosk_recognizer_accept_waveform(this->recognizer, data, length);
}
int VoskRecognizerClass::acceptWaveformShort(const short * data, int length){
    return vosk_recognizer_accept_waveform_s(this->recognizer, data, length);
}
int VoskRecognizerClass::acceptWaveformFloat(const float * data, int length){
    return vosk_recognizer_accept_waveform_f(this->recognizer, data, length);
}
const char * VoskRecognizerClass::result(){
    return vosk_recognizer_result(this->recognizer);
}
const char * VoskRecognizerClass::partialResult(){
    return vosk_recognizer_partial_result(this->recognizer);
}
const char * VoskRecognizerClass::finalResult(){
    return vosk_recognizer_final_result(this->recognizer);
}
void VoskRecognizerClass::reset(){
    return vosk_recognizer_reset(this->recognizer);
}

//VoskBatchModelClass Implementations
VoskBatchModelClass::VoskBatchModelClass(const char * model_path){
    vosk_batch_model_new(model_path);
}
VoskBatchModelClass::VoskBatchModelClass(std::string model_path){
    vosk_batch_model_new(model_path.c_str());
}
VoskBatchModelClass::~VoskBatchModelClass(){
    vosk_batch_model_free(this->batchModel);
}
//Instance methods
void VoskBatchModelClass::wait(){
    vosk_batch_model_wait(this->batchModel);
}    

//VoskBatchRecognizerClass Implemenations
VoskBatchRecognizerClass::VoskBatchRecognizerClass(VoskBatchModelClass batchRecognizer, float sampleRate){
    vosk_batch_recognizer_new(batchRecognizer.batchModel, sampleRate);
}
VoskBatchRecognizerClass::~VoskBatchRecognizerClass(){
    vosk_batch_recognizer_free(this->batchRecognizer);
}
//Instance methods
void VoskBatchRecognizerClass::acceptWaveform(const char * data, int length){
    vosk_batch_recognizer_accept_waveform(this->batchRecognizer,data, length);
}
void VoskBatchRecognizerClass::setNLSML(bool nlsml){
    vosk_batch_recognizer_set_nlsml(this->batchRecognizer, (int)nlsml);
}
void VoskBatchRecognizerClass::finishStream(){
    vosk_batch_recognizer_finish_stream(this->batchRecognizer);
}
void VoskBatchRecognizerClass::frontResult(){
    vosk_batch_recognizer_front_result(this->batchRecognizer);
}
void VoskBatchRecognizerClass::pop(){
    vosk_batch_recognizer_pop(this->batchRecognizer);
}