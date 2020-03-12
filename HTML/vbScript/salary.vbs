option Explicit
On Error Resume Next

Dim NetMonthlySalary

Dim GrossSalary
Dim MonthlyTaxes
MonthlyTaxes = 0.2
Dim MonthlyRetirementContribution
MonthlyRetirementContribution = 0.05

Const Name = "Adam"
Const AnnualSalary = 60000.0


GrossSalary = AnnualSalary/12.0
NetMonthlySalary = GrossSalary - ((GrossSalary * MonthlyTaxes) + (GrossSalary * MonthlyRetirementContribution) + 200)

MsgBox Name & " receives $" & NetMonthlySalary & " as monthly salary after all deductions!!" , 64, "Result:"


