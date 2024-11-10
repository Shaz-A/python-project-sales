#Import the required module-module is a code library/file containing set of functions & classes
import csv
#reads the data from csv file
def read_data():
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data

#print sales of data in a list format
def print_sales_of_data():
    list_of_sales = read_data()
    for sale in list_of_sales:
        print("Sale for the month: {} is {}".format( sale['month'],sale['sales']))

print_sales_of_data()



#Gets Total no of monthly sales and their average
def get_total_sales_and_avg():
    list_of_sales = read_data()
    total_sale = 0
    for sale in list_of_sales:
        sale_int = int(sale['sales'])
        total_sale = total_sale + sale_int
    print('Total sales: {}'.format(total_sale))
    average = 0
    num_of_sales = len(list_of_sales)
    average = total_sale / num_of_sales
    print('The Average of monthly sales : {}'.format(average))


# Main Execution starts here
get_total_sales_and_avg()













