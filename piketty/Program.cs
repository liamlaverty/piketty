using System;

namespace piketty
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            DoUnsafeCode();
        }

       

        private static unsafe void DoUnsafeCode()
        {

            Console.Read();
        }
    }
}
