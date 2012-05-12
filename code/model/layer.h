#ifndef ANIMATOR_MODEL_LAYER_H
#define ANIMATOR_MODEL_LAYER_H

#include "size.h"
#include <string>

using namespace std;


class LayerBase {
    string name;

public:
    LayerBase(string name);
    void setName(string name) { this->name = name; };
    string getName() { return this->name; };
};


class LayerBitmap : public LayerBase {
    int bitDepth;
    Size size;

public:
    LayerBitmap(string name);
    LayerBitmap(string name, int width, int height);
    int getBitDepth() { return this->bitDepth; };
    Size& getSize() { return this->size; };
};

#endif // ANIMATOR_MODEL_LAYER_H
