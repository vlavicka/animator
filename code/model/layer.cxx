#include <iostream>
#include <string>

using namespace std;

#include "layer.h"

LayerBase::LayerBase(string name) 
    : name(name) 
{
}


LayerBitmap::LayerBitmap(string name)
    : LayerBase(name), bitDepth(24)
{
    //this->size.set(0, 0);
    size = Size(0, 0);
}

LayerBitmap::LayerBitmap(string name, int width, int height)
    : LayerBase(name), bitDepth(24)
{
    //this->size.set(width, height);
    size = Size(width, height);
}
