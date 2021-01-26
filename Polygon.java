import java.lang.Math;


public abstract class Polygon {
    protected String name = null;
    protected int sides = 0;
    protected int sideLength = 0;

    public Polygon(String name, int sides, int sideLength) {
        this.name = name;
        this.sides = sides;
        this.sideLength = sideLength;
    }

    public String getName() {
        return name;
    }

    public int getSides() {
        return sides;
    }

    public int getSideLength() {
        return sideLength;
    }

    public int getPerimeter() {
        return sideLength * sides;
    }

    public int getAngle() {
        return (sides - 2) * 180 / sides;
    }

    public abstract int getArea();

    public String toString() {
        return name + "(" + sideLength + ")";
    }

    public static void main(String[] args) {
        Triangle triangle = new Triangle(5);
        System.out.println(triangle);
        System.out.println("getName(): " + triangle.getName());
        System.out.println("getSides(): " + triangle.getSides());
        System.out.println("getSideLength(): " + triangle.getSideLength());
        System.out.println("getArea(): " + triangle.getArea());
        System.out.println("getPerimeter(): " + triangle.getPerimeter());
        System.out.println("getAngle(): " + triangle.getAngle());
    }
}


class Triangle extends Polygon {
    public Triangle(int sideLength) {
        super("Triangle", 3, sideLength);
    }

    public int getArea() {
        int base = sideLength;
        int height = (sideLength / 2) * (int) Math.sqrt(3);
        int area = base * height / 2;
        return area;
    }

}
