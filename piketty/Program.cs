using System;
using System.Runtime.InteropServices;

namespace piketty
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            DoUnsafeIntCode();

            DoUnsafeArrayCode();

            Console.WriteLine("finished");
            Console.Read();


        }


        
        



        private static unsafe void DoUnsafeArrayCode()
        {
            int[] y = new int[] { 3, 4, 5 };

       
        }


        /// <summary>
        /// Creates an int and a pointer to it
        ///
        /// Adds 1 directly to the int and prints it
        ///
        /// Adds 1 to the pointer and prints the original int
        /// </summary>
        private static unsafe void DoUnsafeIntCode()
        {
            int numberX =100;

            int* ptrX = &numberX;

            Console.WriteLine($"pointer {nameof(ptrX)} = {numberX} should = 100");

            numberX++;
            Console.WriteLine($"pointer {nameof(ptrX)} = {numberX} should = 101");

            *ptrX = 102;
            Console.WriteLine($"pointer {nameof(ptrX)} = {numberX} should = 102");
        }
    }


    public class OtherClass
    {
        /// <summary>
        /// a private int that can't be changed outside
        /// this class
        /// </summary>
        private int ValX { get; }

        public OtherClass(int valX)
        {
            ValX = valX;
        }


        /// <summary>
        /// Just prints x
        /// </summary>
        public void PrintValX()
        {
            Console.WriteLine($"ValX = {ValX}");
        }
    }
}
