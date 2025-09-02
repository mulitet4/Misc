class CustomException extends Exception{
  int num;
  CustomException(int n){
    num = n;
  }

  public String toString(){
    return "Error occurred. Entered number is " + num;
  }
}

interface Series {
  int getValue() throws CustomException;
}

class Series1 implements Series {
  public int getValue() throws CustomException{
    if(true == true){

    throw new CustomException(55);
    }
    return 0;
  }
}


class ErrorDemo {
  public static void main(String[] args){
    Series s;
    s = new Series1();
    try {

    s.getValue();
    } catch(Exception e){
      System.out.println(e);
    }
  }
}