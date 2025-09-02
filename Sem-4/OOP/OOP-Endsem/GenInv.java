class so{
    static void pln(Object o){System.out.println(o.toString());}
}

class withId {
    int id;
    withId(int i){id = i;}
}

class genericInventory<T extends withId> {
    T[] arr;
    
    genericInventory(T[] a){
        arr = a;
    }
    
    T getItem(int id){
        for(T item: arr){
            if(item.id == id){
                return item;
            }
        }
        so.pln("Item not found.");
        return arr[0];
    }
    
    void sort(){
        for(int i = 0; i < arr.length - 1; i++){
            for(int j = 0; j < arr.length - 1; j++){
                if(arr[j].id > arr[j+1].id){
                    T temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
}

class ElectronicDevice extends withId{
    int watt;
    ElectronicDevice(int id, int w){
        super(id);
        watt = w;
    }
    void display(){
        so.pln("ID: " + id + " Watt: " + watt);
    }
}

class ClothingItem extends withId{
    String size;
    ClothingItem(int id, String s){
        super(id);
        size = s;
    }
    void display(){
        so.pln("ID: " + id + " Size: " + size);
    }
}

class Main {
    public static void main(String[] args) {
        ClothingItem carr[] = {new ClothingItem(3, "Md"), new ClothingItem(5, "Lg"), new ClothingItem(1, "Sm")};
        ElectronicDevice earr[] = {new ElectronicDevice(5, 220), new ElectronicDevice(2, 220), new ElectronicDevice(6, 220)};
        genericInventory<ClothingItem> gi1 = 
            new genericInventory<ClothingItem>(carr);
        genericInventory<ElectronicDevice> gi2 = 
            new genericInventory<ElectronicDevice>(earr);
        so.pln("");
        gi2.getItem(5).display();
        
        gi2.arr[0].display();
        gi2.arr[1].display();
        gi2.arr[2].display();
        
        gi2.sort();
        
        gi2.arr[0].display();
        gi2.arr[1].display();
        gi2.arr[2].display();
    }
}

// ID: 5 Watt: 220
// ID: 5 Watt: 220
// ID: 2 Watt: 220
// ID: 6 Watt: 220
// ID: 2 Watt: 220
// ID: 5 Watt: 220
// ID: 6 Watt: 220