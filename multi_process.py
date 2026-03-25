import csv
import subprocess

csv_file = "dataset_meta.csv"  # path to your CSV

with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        # skip row starting with "#"
        if row[0][0] == "#":
            continue

        # get plot id
        plot_id = row[0].strip()

        # get dates
        if len(row) == 2 and "," in row[1]:
            dates = [d.strip() for d in row[1].split(",") if d.strip()]
        else:
            dates = [col.strip() for col in row[1:] if col.strip()]

        # exclude any date containing the letter "x" (case-insensitive)
        dates = [d for d in dates if 'x' not in d.lower()]

        # Execute main script
        for j in range(len(dates)):

            cmd = ["python3", "main.py", "--plot_id", plot_id, "--date", dates[j]]
            try:
                subprocess.run(cmd, check=True)
                print(f"Executed: python3 main.py --plot_id {plot_id} --date {dates[j]}")
            except subprocess.CalledProcessError as e:
                print(f"Error executing: python3 main.py --plot_id {plot_id} --date {dates[j]}")
                print(e)

                