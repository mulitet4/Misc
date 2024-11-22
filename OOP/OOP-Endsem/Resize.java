class so{
    static void pln(Object o){System.out.println(o.toString());}
}

interface Resizable {
    void resizeWidth(int width);
    void resizeHeight(int height);
}

class Rectangle implements Resizable {
    int height;
    int width;
    Rectangle(int h, int w){
        height = h;
        width = w;
    }
    public void resizeWidth(int w){width = w;}
    public void resizeHeight(int h){height = h;}
}

class Main {
    public static void main(String[] args) {
        Rectangle r = new Rectangle(5, 6);
        so.pln(r.width);
        r.resizeWidth(7);
        so.pln(r.width);
    }
}