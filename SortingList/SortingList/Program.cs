using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SortingList
{
    class Program
    {
        static void Main(string[] args)
        {
            //{ 5, 3, 6, 2, 10};
            int[] numbers = { 5, 3, 6, 2, 10 };
            int i;

            int findLower()
            {
                int lower, lowerIndex;
                lower = numbers[0];
                lowerIndex = 0;

                for (i = 0; i < numbers.Length; i++)
                {
                    if (numbers[i] < lower)
                    {
                        lower = numbers[i];
                        lowerIndex = i;
                    }

                }
                return lower;

            }

                int findHigher()
                {
                    int higher = 0;

                    for (i = 0; i < numbers.Length; i++)
                    {
                        if (numbers[i] > higher)
                        {
                            higher = numbers[i];

                        }

                    }
                    return higher;
                }

            findLower();
            findHigher();
            Console.WriteLine("The Lower number of the array is: "+ findLower());
            Console.WriteLine("The Higher number of the array is: "+ findHigher());


            Console.ReadKey();

        }
    }
}
