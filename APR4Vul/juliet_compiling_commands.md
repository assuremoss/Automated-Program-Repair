## Experimenting juliet dataset on Linux (Ubuntu)
- Ubuntu 16.04
- javac 1.8.0_191
- Juliet Test Suite for Java version 1.3

1. Compiling a specific test case
```console
foo@bar:~/RepairThemAll/benchmarks/juliet/src$  sudo javac -cp ../lib/servlet-api.jar:../lib/commons-lang-2.5.jar:../lib/commons-codec-1.5.jar:../lib/javamail-1.4.4.jar testcasesupport/IO.java testcasesupport/AbstractTestCaseBase.java testcasesupport/AbstractTestCase.java testcasesupport/AbstractTestCaseBadOnly.java testcasesupport/AbstractTestCaseServletBase.java testcasesupport/AbstractTestCaseServlet.java testcasesupport/AbstractTestCaseServletBadOnly.java testcasesupport/AbstractTestCaseClassIssue.java testcasesupport/AbstractTestCaseClassIssueBad.java testcasesupport/AbstractTestCaseClassIssueGood.java testcases/CWE78_OS_Command_Injection/CWE78_OS_Command_Injection__console_readLine_01.java
```
2. Checking if the compilation successes
```console
// There will be a generated class file in the directory containing source file
foo@bar:~/RepairThemAll/benchmarks/juliet/src$ ls testcases/CWE78_OS_Command_Injection | grep CWE78_OS_Command_Injection__console_readLine_01.class
CWE78_OS_Command_Injection__console_readLine_01.class
```

3. Executing the compiled test case above
```console
foo@bar:~/RepairThemAll/benchmarks/juliet/src$ java -cp ../lib/servlet-api.jar:../lib/commons-lang-2.5.jar:../lib/commons-codec-1.5.jar:../lib/javamail-1.4.4.jar:. testcases.CWE78_OS_Command_Injection.CWE78_OS_Command_Injection__console_readLine_01
Starting tests for Class testcases.CWE78_OS_Command_Injection.CWE78_OS_Command_Injection__console_readLine_01
Completed good() for Class testcases.CWE78_OS_Command_Injection.CWE78_OS_Command_Injection__console_readLine_01

Completed bad() for Class testcases.CWE78_OS_Command_Injection.CWE78_OS_Command_Injection__console_readLine_01
```
 
