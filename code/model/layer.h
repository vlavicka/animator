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
