"""
Improved script to convert auto-mpg.data to a clean CSV file
"""

def convert_auto_mpg_to_csv(input_file, output_file):
    """
    Converts the UCI Auto MPG dataset from space-delimited format to CSV.
    Properly handles missing values (marked as "?") by converting them to empty strings.
    
    Parameters:
    input_file (str): Path to the original auto-mpg.data file
    output_file (str): Path where the CSV file will be saved
    """
    # Define column names for the header
    header = "mpg,cylinders,displacement,horsepower,weight,acceleration,model_year,origin,car_name\n"
    
    # Open both files
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Write the header to the output file
        outfile.write(header)
        
        # Process each line
        for line in infile:
            if not line.strip():
                continue  # Skip empty lines
            
            # Extract the car name (everything between quotes)
            if '"' in line:
                parts = line.split('"')
                data_part = parts[0].strip()
                car_name = parts[1]
            else:
                data_part = line.strip()
                car_name = ""
            
            # Split the data part by whitespace
            values = data_part.split()
            
            # Make sure we have at least 8 values (excluding car name)
            if len(values) < 8:
                continue
            
            # Replace "?" with empty string (will be interpreted as NaN by pandas)
            for i in range(len(values)):
                if values[i] == "?":
                    values[i] = ""
            
            # Create a CSV line
            csv_values = values[:8]  # Get the first 8 values
            csv_line = ','.join(csv_values) + f',"{car_name}"\n'
            
            # Write the line to the output file
            outfile.write(csv_line)
    
    print(f"Conversion complete. CSV file saved to {output_file}")

if __name__ == "__main__":
    input_file = "auto-mpg.data"      # Path to your input file
    output_file = "auto-mpg.csv"      # Path where output will be saved
    
    convert_auto_mpg_to_csv(input_file, output_file)