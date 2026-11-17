def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as d:
        for line in d:
            list_line = line.split(",")
            if list_line[0] == "supply":
                supply += int(list_line[1])
            if list_line[0] == "buy":
                buy += int(list_line[1])
        d.close()

    result = supply - buy

    with open(report_file_name, "a") as r:
        r.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
