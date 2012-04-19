#ifndef ANIMATOR_MODEL_LAYER_H
#define ANIMATOR_MODEL_LAYER_H
#include "layer.h"

LayerBase::LayerBase(int number) 
    : number(number)
{ 
    this->number = number;
}

LayerBitmap::LayerBitmap(int number)
    : LayerBase(number)
{
    this->bitDepth = 24;
}

#endif // ANIMATOR_MODEL_LAYER_H
