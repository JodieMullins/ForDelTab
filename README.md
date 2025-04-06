# Store Sales

Store data includes at start of project: 

    - sales representatives and regional areas

    - orders placed and customers delivered to

    - orders returned

Columns created / calculated: 
    - Month (pulled from serialized date)

    - Year (pulled from serialized date)

    - Quarter assigned to Month based on logic within IFS function

    - Number of days for delivery calculated

    - Ship method simplified to one word entries
    

Goals: 
    - Determine Sales Growth KPI

        > Sales Growth = (Current period sales - Sales during past period) / Sales during past period x 100

            > Requires breaking down current sales data into quarterly sections
                [x] Completed via Excel

    - Hone in on Returns 

        > Segment, State, Category, and Product Name

            > Questions to ask in the effort of improvement:
            1) Which segment of consumer is most often returning?
            2) Is there a geographical area items are returned from most?
            3) Is there a particular category that is most frequently returned?
            4) Does one product get returned more than others?  

    - Considering the sales growth, would it make sense to split the West into two separate regions of the West and Northwest?