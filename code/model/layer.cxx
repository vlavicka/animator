#include <iostream>
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

