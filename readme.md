Biased Random generator
the functioning and usage is explained in this readme file
no third part or predefined random generation libraries are used
libraby time is used for getting time in kicks to get a new seed every time for the random number generation algorithm.


1)generation of pseudorandom numbers is done by using Linear Congruential generator algorithm by using modulo arithmetic X(n+1) = (aXn + c) mod m


Explanation:>

	the biasing for number selection is done by probability 
	by using 27 L's and 73 H's in a list of size 100 (27+73) and
	then randomly selecting alphabet from the list we attain a probability of
	27% for Lows(L) and 73% for Highs(H) and then accoring to outcome of L or H
	we can then randomly select a number from the upper half of list or the 
	lower half of the list depending on the outcome of L or H.
	EXAMPLE:
		suppose a list from 1 to 10
		and we got H from probability then the by dividing the list in two parts we get two portions 
		of lists one higher than 5 and the other lower than 5,
		then as we got H so we select a number between 5 and 10,
		obtaining a biased random number towards greater number i.e. 10 at probability of 73%

for using the python script :
	run the script
	enter the lower limit when asked (i.e. for list of 1 to 10 enter 1)
	enter the upper limit when asked (i.e. for list of 1 to 10 enter 10)
	press enter and the outcome will be 73% biased to the larger number

	 