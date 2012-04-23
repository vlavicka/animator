#include <iostream>
#include <string>

using namespace std;

#include "size.h"
#include "layer.h"

#ifndef USESWIG
#include <iostream>
int main()
{
    return 0;
}
#endif

LayerBase::LayerBase(string name) 
    : name(name) 
{
}


LayerBitmap::LayerBitmap(string name)
    : LayerBase(name), bitDepth(24)
{
    size = Size(0, 0);
}

LayerBitmap::LayerBitmap(string name, int width, int height)
    : LayerBase(name), bitDepth(24)
{
    size = Size(width, height);
}
