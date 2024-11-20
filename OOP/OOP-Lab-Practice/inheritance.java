class so {
  public static void pln(Object o){System.out.println(o.toString());}
}

class Student {
  private String name;
  private int rollno;
  private int marks[];

  Student(String n, int r, int m[]){
    name = n;
    rollno = r;
    marks = m;
  }
}

class ScienceStudent extends Student{
  int scienceMarks;

  ScienceStudent(String n, int r, int m[], int s){
    super(n, r, m);
    scienceMarks = s;
  }

  void display(){
    so.pln(scienceMarks);
  }
}

class Main {
  public static void main(String[] args){
    ScienceStudent s;
    int m[] = {1,2,3,4};
    s = new ScienceStudent("Aaryab", 36, m, 55);
    s.display();
  }
}