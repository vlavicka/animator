#ifndef ANIMATOR_MODEL_LAYER_H
#define ANIMATOR_MODEL_LAYER_H

class LayerBase
{
    public:
    int number;
    LayerBase(int number);
};

class LayerBitmap : public LayerBase
{
    public:
    int bitDepth;
    LayerBitmap(int number);
};

#endif // ANIMATOR_MODEL_LAYER_H
