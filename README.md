<h1> Quora Trend Analyzer </h1> 

<h3> ABOUT </h3>

<p> The goal is to design and implement a trend analysis engine. This engine should be able to take as input a table of raw data and present an interface for trend analysis. You are free to design this interface and choose the data analysis features that you wish to support. It is important that the engine only exposes to the user data that does not have any personal identifiers and protects sensitive attributes from being revealed.</p>

<p> The full listing is <a href="http://www.quora.com/challenges#trend_analyzer" </a>available here</p>

<h2>QUICKSTART: </h2>

>Clone the respository and inside the root folder run
>
>python main.py ~/filepath/filename.csv
>
>
> The whitehouse.csv and hospital.csv are the best testing files given, as airquality was not of the proper format. 
>
> Note: this is written in Python 3


<h3> Documentation notes </h3>

<p> This program takes in a file format: first row - column names, second row - datatypes, remaing rows - data. There are columns that possess sensitive information that are not accessable. Column plots are generated first first to assess column variation. Columns containing strings are assessed based on their first character while sensitive information undergoes an encoding process. Following visual assessment, the program displays interrogation, sampling or sorting options of the file. The user can get a better feel for their dataset and
    write an ouputfile that better suits their needs. </p>

> sample - prints a random sample of the dataset
>
> interrogate - asks for column(s) to report the most and least frequent values
>
> sort - sorts data using specified column 
>
> write - writes a new dataset with the option of deleting columns or being sorted by a column 

<h5> This is under general GNU General Public Licence. </h5>