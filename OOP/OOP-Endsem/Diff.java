class so{
    static void pln(Object o){System.out.println(o.toString());}
}

class Diff{
    static int min_diff(int[] a){
        int min = 99;
        for(int i = 0; i < a.length - 1; i++){
            int diff = a[i+1] - a[i];
            if(min > diff) min = diff;
        }
        return min;
    }
}

class Main {
    public static void main(String[] args) {
        int[] a = {1, 5, 9, 15};
        int m = Diff.min_diff(a);
        so.pln(m);
    }
}

// 4