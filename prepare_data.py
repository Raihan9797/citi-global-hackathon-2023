 
def prepare_clients(clients):
    client_cols = list(clients.columns)
    client_cols
    clients = clients.rename(columns={
        'Client Name': 'client_name',
        'Company': 'company',
        'Industry': 'industry',
        'Region': 'region',
        'Years with Bank': 'years_with_bank'
    })
    return clients

def prepare_deals(deals):
    # deal_cols = list(deals.columns)
    deals = deals.rename(columns={
    'Deal ID': 'deal_id',
    'Product': 'product_name',
    'Country': 'country',
    'Client (Person)': 'client_person',
    'Client (Company)': 'client_company',
    'Bank Employee Contact': 'bank_employee_contract',
    'Start Date': 'start_date',
    'End Date': 'end_date',
    'Deal Type': 'deal_type'
    })
    return deals

def prepare_employees(employees):
    employees = employees.rename(columns={
        'Employee Name': 'employee_name',
        'Company Department': 'company_department',
        'Industry': 'industry',
        'Region': 'region',
        'Client Capacity (Count)': 'client_capacity_count',
        'Experience (Years)': 'experience_years',
        'Designation': 'designation'
    })
    return employees 

def filter_deals(
    deal_df,
    # deal_id',
    product,
    country,
    # client_person',
    # client_company',
    # bank_employee_contract',
    # start_date',
    # end_date',
    deal_type
):
    res =deal_df[deal_df.product_name.str.contains(product) 
                 & deal_df.country.str.contains(country) 
                 & deal_df.deal_type.str.contains(deal_type)]
    return res

def filter_clients(
    client_df,
    region,
    industry,
    deal_type
):
    res =client_df[client_df.region.str.contains(region) 
                 & client_df.industry.str.contains(industry) 
                #  & client_df.deal_type.str.contains(deal_type)
                 ]
    return res

def filter_employees(
    emp_df,
    region,
    industry,
    deal_type
):
    # print(emp_df)
    res =emp_df[emp_df.region.str.contains(region) 
                 & emp_df.industry.str.contains(industry) 
                 & emp_df.designation.str.contains(deal_type)
                 ]
    print(res)
    return res