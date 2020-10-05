import numpy as np
from scipy.stats import expon, t

n_repetitions = 2 #Number of repetitions

def SingleServerQueueSimulator():
    job_index = 0
    arrival_times, service_times, departures, delay_times = [], [], [], []

    while True:
        delay_times.append(0)
        departures.append(0)
        job_entry_arrival = expon.rvs(scale = (5/10), loc=0, size=1)

        if(job_index == 0):
            arrival_times.append(job_entry_arrival)
        else:
            arrival_times.append(arrival_times[job_index-1] + job_entry_arrival)
        
        service_times.append(expon.rvs(scale = (6/10), loc=0, size=1))

        if(arrival_times[job_index] < departures[job_index -1]):
            delay_times[job_index] = departures[job_index -1] - arrival_times[job_index]
        else:
            departures[job_index] = 0.0

        departures[job_index] = arrival_times[job_index] + delay_times[job_index] + service_times[job_index]

        if departures[job_index] == 600 or departures[job_index] >= 600:
            break

        job_index+=1

    return arrival_times, service_times, delay_times, departures, len(departures)


def average(data_array):
    return sum(data_array) / len(data_array)

def ConfidenceInterval(data, t):
    n = len(data)
    ds = np.std(data)

    denominator = pow(n-1 , 1/2)
    sample = average(data)

    li = sample - (t*ds/denominator)
    ls = sample + (t*ds/denominator)
    return li , ls

def repetition(iterations) :

    length_results, average_interarrival_time_results, arrival_rate_results, average_service_times_results, service_rate_results, average_delay_results, average_wait_results, time_average_queue_results, time_average_service_results, time_average_node_results = [],[],[],[],[],[],[],[],[],[]

    for i in range(iterations):
        arrival_times, service_times, delay_times, departures, length = SingleServerQueueSimulator()

        average_interarrival_time = arrival_times[length - 1] / length
        average_service_time = average(service_times)
        average_delay_time = average(delay_times)
        average_wait_time = average_delay_time + average_service_time
        time_average_queue = (average_delay_time * length) / departures[length - 1]
        time_average_service = (average_service_time * length) / departures[length - 1]

        average_interarrival_time_results.append(average_interarrival_time)
        arrival_rate_results.append(1/average_interarrival_time)
        average_service_times_results.append(average_service_time)
        service_rate_results.append(1/average_service_time)
        average_delay_results.append(average_delay_time)
        average_wait_results.append(average_wait_time)


        time_average_queue_results.append(time_average_queue)
        time_average_service_results.append(time_average_service)
        time_average_node_results.append(time_average_queue + time_average_service)

        length_results.append(length)

    return length_results, average_interarrival_time_results, arrival_rate_results, average_service_times_results, service_rate_results, average_delay_results, average_wait_results, time_average_queue_results, time_average_service_results, time_average_node_results


print('Calculating statistics, please wait...')
length_results, average_interarrival_time_results, arrival_rate_results, average_service_times_results, service_rate_results, average_delay_results, average_wait_results, time_average_queue_results, time_average_service_results, time_average_node_results = repetition(n_repetitions)

averages_table  = []

avg_length = average(length_results)
avg_interarrival_time_results = average(average_interarrival_time_results)
avg_arrival_rate_results = average(arrival_rate_results)
avg_service_times_results = average(average_service_times_results)
avg_service_rate_results = average(service_rate_results)
avg_delay_results = average(average_delay_results)
avg_wait_results = average(average_wait_results)
avg_time_average_queue_results = average(time_average_queue_results)
avg_time_average_service_results = average(time_average_service_results)
avg_time_average_node_results = average(time_average_node_results)


alfa = 0.05
t_value = t.ppf(1-(alfa/2), len(average_interarrival_time_results) - 1)


averages_table.append(['Statistic Name', 'Average', 'Confidence Interval'])
li,ls = ConfidenceInterval(length_results,t_value)
averages_table.append(['Jobs average', float(avg_length), "{0} - {1}".format(float(li),float(ls))])
li,ls = ConfidenceInterval(average_interarrival_time_results,t_value)
averages_table.append(['Inter-arrival time average', float(avg_interarrival_time_results), "{0} - {1}".format(float(li),float(ls))])
li,ls = ConfidenceInterval(arrival_rate_results,t_value)
averages_table.append(['Inter-arrival rate average', float(avg_arrival_rate_results), "{0} - {1}".format(float(li),float(ls))])
li,ls = ConfidenceInterval(average_service_times_results,t_value)
averages_table.append(['Service average', float(avg_service_times_results), "{0} - {1}".format(float(li),float(ls))])
li,ls = ConfidenceInterval(service_rate_results,t_value)
averages_table.append(['Service rate average', float(avg_service_rate_results), "{0} - {1}".format(float(li),float(ls))])
li,ls = ConfidenceInterval(average_delay_results,t_value)
averages_table.append(['Delay time average', float(avg_delay_results), "{0} - {1}".format(float(li),float(ls))])
li,ls = ConfidenceInterval(average_wait_results,t_value)
averages_table.append(['Wait time average', float(avg_wait_results), "{0} - {1}".format(float(li),float(ls))])
li,ls = ConfidenceInterval(time_average_queue_results,t_value)
averages_table.append(['Time-averaged number in the node average', float(avg_time_average_queue_results), "{0} - {1}".format(float(li),float(ls))])
li,ls = ConfidenceInterval(time_average_service_results,t_value)
averages_table.append(['Time-averaged number in the queue average', float(avg_time_average_service_results), "{0} - {1}".format(float(li),float(ls))])
li,ls = ConfidenceInterval(time_average_node_results,t_value)
averages_table.append(['Time-averaged number in the service average', float(avg_time_average_node_results), "{0} - {1}".format(float(li),float(ls))])

for statistic_name, value, confidence_interval in averages_table:
    print ("{:<45} {:<20} {:<20}".format(statistic_name, value, confidence_interval))