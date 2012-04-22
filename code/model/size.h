#ifndef ANIMATOR_MODEL_SIZE_H
#define ANIMATOR_MODEL_SIZE_H

class Size {
    int width;
    int height;
public:
    Size() : width(0), height(0) {};
    Size(int w, int h);

    int getWidth() { return width; };
    int getHeight() { return height; };

    void set(int w, int h);
    void setWidth(int w);
    void setHeight(int h);
};

#endif // ANIMATOR_MODEL_SIZE_H
