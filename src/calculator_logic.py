def get_net_salary(gross_annual_salary :float, pf_mode :int, basic_annual_salary = None, paytm_foodwallet = None):
  annual_gratuity  = 20448
  annual_pro_tax = 2500
  other_annual_deductions = annual_gratuity + annual_pro_tax
  annual_pf_cut = 0
  if paytm_foodwallet:
    other_annual_deductions += paytm_foodwallet
  if pf_mode == 0:
    pf_monthly_cut = round(0.12 * 15000 * 2)
    annual_pf_cut = pf_monthly_cut * 12
    # net_annual_salary = gross_annual_salary - annual_pf_cut
  elif pf_mode == 1:
    annual_pf_cut = round(0.12 * basic_annual_salary * 2)
  net_annual_salary = gross_annual_salary - annual_pf_cut
  net_annual_salary -= other_annual_deductions
  net_salary = net_annual_salary // 12
  print('You pay annual PF : ', annual_pf_cut)
  # print(f'Net annual salary : {net_annual_salary:,}')
  return net_salary

def get_take_home_OR(net_annual_salary):
  slabs = [250000, 500000,750000, 1000000, 1250000, 1500000]
  rates = [0, 0.05, 0.2, 0.2, 0.3, 0.3, 0.3]
  if net_annual_salary < slabs[0]:
    taxable_amt = 0
    annual_tax_amt = taxable_amt * rates[0] #0%
    tax_slab = slabs[0]
    tax_rate = rates[0]
    #btw 2.5 and 5
  elif slabs[0] < net_annual_salary < slabs[1]:
    taxable_amt = net_annual_salary - slabs[0]
    annual_tax_amt = taxable_amt * rates[1] #5%
    tax_slab = slabs[1]
    tax_rate = rates[1]
    #btw 5 and 7.5
  elif slabs[1] < net_annual_salary < slabs[2]:
    taxable_amt = net_annual_salary - slabs[1]
    annual_tax_amt = taxable_amt * rates[2] #20%
    tax_slab = slabs[2]
    tax_rate = rates[2]
  #btw 7.5 and 10
  elif slabs[2] < net_annual_salary < slabs[3]:
    taxable_amt = net_annual_salary - slabs[2]
    annual_tax_amt = taxable_amt * rates[3] #20%
    tax_slab = slabs[3]
    tax_rate = rates[3]
    #btw 10 and 12.5
  elif slabs[3] < net_annual_salary < slabs[4]:
    taxable_amt = net_annual_salary - slabs[3]
    annual_tax_amt = taxable_amt * rates[4] #30%
    tax_slab = slabs[4]
    tax_rate = rates[4]
    #btw 12.5 and 15
  elif slabs[4] < net_annual_salary < slabs[5]:
    taxable_amt = net_annual_salary - slabs[4]
    annual_tax_amt = taxable_amt * rates[5] #30%
    tax_slab = slabs[5]
    tax_rate = rates[5]
  else:
    #above 15
    taxable_amt = net_annual_salary - slabs[5]
    annual_tax_amt = taxable_amt * rates[6]
    tax_slab = 1500001
    tax_rate = rates[6]
  
  print(f'You are in tax slab : UPTO {tax_slab:,} with tax rate : {tax_rate * 100} % ')
  annual_tax_amt = round(annual_tax_amt)
  print(f'Your annual tax amount : {annual_tax_amt:,}')
  take_home_annual_salary = (net_annual_salary - annual_tax_amt)
  print(f'Net annual salary : {net_annual_salary:,}')
  print(f'Net annual take home salary : {take_home_annual_salary:,}')
  print(f'Net monthly take home salary : {take_home_annual_salary//12:,}')
  print('*' * 50)
  return take_home_annual_salary//12, annual_tax_amt
  
def percent_change(small, big):
  frac_diff = (big - small)/small
  percent_rise = round(frac_diff * 100,2)
  # print(f'There is {percent_rise} % rise in between two options')
  return percent_rise
  
def find_take_home_OR(gross_annual_salary, pf_mode, basic_annual_salary = None, paytm_foodwallet = None):
  mode_n_monthly_salary = get_net_salary(gross_annual_salary, pf_mode, basic_annual_salary, paytm_foodwallet)
  annual_salary_mode_n = mode_n_monthly_salary * 12
  take_home_OR_n, annual_tax_amt = get_take_home_OR(annual_salary_mode_n)
  percent_change_from_gross = percent_change(gross_annual_salary//12, take_home_OR_n)
  print(f'Percent change in salary wrt to gross : {percent_change_from_gross} %')
  return take_home_OR_n, annual_tax_amt