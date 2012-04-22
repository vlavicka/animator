#include <cassert>
#include "size.h"

void Size::set(int w, int h) {
    this->setWidth(w);
    this->setHeight(h);
}

Size::Size(int w, int h) {
    this->set(w, h);
}

void Size::setWidth(int w) { 
    assert(w >= 0);
    this->width = w; 
}

void Size::setHeight(int h) { 
    assert(h >= 0);
    this->height = h; 
}
