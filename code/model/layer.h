#ifndef ANIMATOR_MODEL_LAYER_H
#define ANIMATOR_MODEL_LAYER_H

using namespace std;


class Size {
    int width;
    int height;
public:
    Size() : width(0), height(0) {};
    Size(int w, int h) : width(w), height(h) {};
    int getWidth() { return this->width; };
    void setWidth(int w) { this->width = w; };
    int getHeight() { return this->height; };
    void setHeight(int h) { this->height = h; };
    void set(int w, int h) { this->width = w; this->height = h; };
};

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
    Size * getSize() { return &this->size; };
};

#endif // ANIMATOR_MODEL_LAYER_H
