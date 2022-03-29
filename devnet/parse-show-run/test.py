from ciscoconfparse import CiscoConfParse
import csv

parse = CiscoConfParse('show-run.txt',syntax='ios')

for intf_obj in parse.find_objects('^interface'):
   intf_name = intf_obj.re_match_typed('^interface\s+(\S.+?)$')
   intf_desc = intf_obj.re_match_iter_typed(
       '^\s+description\s+(\S.+?)$', result_type=str,
       group=1, default=''
   )
   print("{0}:{1}".format(intf_name, intf_desc))


   """ Write to a .csv file """

   file_output = open('file_output.csv', mode='a', newline='')
   csv_writer = csv.writer(file_output, delimiter=',')

   csv_writer.writerow([intf_name, intf_desc])
   file_output.close()



