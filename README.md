<h1> Quora Trend Analyzer </h1> 

<h3> ABOUT </h3>

<p> The goal is to design and implement a trend analysis engine. This engine should be able to take as input a table of raw data and present an interface for trend analysis. You are free to design this interface and choose the data analysis features that you wish to support. It is important that the engine only exposes to the user data that does not have any personal identifiers and protects sensitive attributes from being revealed... </p>

<p> The full listing is <a href="http://www.quora.com/challenges#trend_analyzer" </a>available here</p>

<h2>QUICKSTART: </h2>

>Clone the respository and inside the root folder run
>
>python main.py ~/filepath/filename.csv
>
>
> The whitehouse.csv is the best testing file given. As airquality was not of the proper input. 
>Note: this is written in Python 3 </p>


<h3> Documentation notes </h3>

<p> This program takes in a file with the first row being column IDs and the second row being datatypes. There are columns that possess sensitive information which are not aloud to be accessed. The program first plots columns variation of the file followed by the option to interrogate, write, sample or sort the file. </p>

> sample - prints a random sample of the dataset
>
> interrogate - asks for column(s) to report the most and least frequent values
>
> sort - sorts data using specified column 
>
> write - writes a new dataset with the option of deleting columns or being sorted by a column 