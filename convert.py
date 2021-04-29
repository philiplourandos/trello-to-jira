#!/bin/python3

import csv
import json
import sys
import jsonpath_rw_ext
from jsonpath_ng.ext import parse

inputFile = sys.argv[1]

print(f"Input file: {inputFile}")

csvHeader = [   'Summary','Issue key','Issue id','Parent id','Issue Type','Status','Project key',
                'Project name','Project type','Project lead','Project lead id','Project description','Project url', 'Priority',
                'Resolution','Assignee','Assignee Id','Reporter','Reporter Id','Creator','Creator Id',
                'Created','Updated','Last Viewed','Resolved','Affects versions','Fix versions','Fix versions',
                'Components','Components','Due date','Votes','Labels','Labels','Labels',
                'Description','Environment','Watchers','Watchers','Watchers','Watchers','Watchers',
                'Watchers','Watchers','Watchers Id','Watchers Id','Watchers Id','Watchers Id','Watchers Id',
                'Watchers Id','Watchers Id','Original estimate','Remaining Estimate','Time Spent','Work Ratio','Σ Original Estimate',
                'Σ Remaining Estimate','Σ Time Spent','Security Level','Outward issue link (Blocks)','Outward issue link (Blocks)','Outward issue link (Blocks)','Outward issue link (Blocks)',
                'Outward issue link (Blocks)','Outward issue link (Blocks)','Outward issue link (Blocks)','Outward issue link (Blocks)','Outward issue link (Blocks)','Outward issue link (Cloners)','Outward issue link (Duplicate)',
                'Outward issue link (Issue split)','Outward issue link (Relates)','Outward issue link (Relates)','Attachment','Attachment','Attachment','Attachment',
                'Attachment','Attachment','Attachment','Attachment','Attachment','Attachment','Attachment',
                'Attachment','Attachment','Custom field (Bug Category)','Custom field (Bug Type)','Custom field (Change completion date)','Custom field (Change reason)', 'Custom field (Change risk)',
                'Custom field (Change start date)','Custom field (Change type)i','Custom field (Development)','Custom field (End date)','Custom field (Epic Color)','Custom field (Epic Link)','Custom field (Epic Name)',
                'Custom field (Epic Status)','Custom field (FOS_Ref)','Custom field (Impact)','Custom field (Issue color)','Custom field (Quantify Time Spent (h))','Custom field (Rank)','Custom field (Request Type)',
                'Custom field (Root Cause)','Custom field (Root Cause)','Custom field (Root cause)','Custom field (Route Cause Description)','Sprint','Sprint','Sprint',
                'Custom field (Start date)','Custom field (Story Points)','Custom field (Story point estimate)','Custom field (Target end)','Custom field (Target start)','Custom field (Team)',
                'Custom field ([CHART] Date of First Response)','Comment','Comment','Comment','Comment','Comment','Comment',
                'Comment','Comment','Comment','Comment','Comment','Comment','Comment',
                'Comment','Comment','Comment','Parent','Parent summary','Status Category']

with open(inputFile, "r", encoding="UTF-8") as reader:
    jsonContent = json.load(reader)

    cards = jsonpath_rw_ext.match('$.cards', jsonContent)
    data = cards[0]

    totalCards = len(cards[0])

    if totalCards > 0:
        with open('jira.csv', 'w', newline='') as csvfile:
            ticketWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            ticketWriter.writerow(csvHeader)

            ticketWriter.writerow(csvHeader)

            for cardIndex in range(totalCards):
                currentCard = data[cardIndex]
                ticketWriter.writerow(
                        currentCard['name'], #summary
                        currentCard[''], #issue key
                        currentCard[''], #issue id
                        currentCard[''], #parent id
                        currentCard[''], #issue type
                        currentCard[''], #status
                        currentCard[''], #Project Key
                        currentCard[''], #project name
                        currentCard[''], #project type
                        currentCard[''], #project lead
                        currentCard[''], #project lead id
                        currentCard[''], #project description
                        currentCard[''], #project url
                        currentCard[''], #priority
                        currentCard[''], #resolution
                        currentCard[''], #assignee
                        currentCard[''], #assignee id
                        currentCard[''], #Reporter
                        currentCard[''], #reporter id
                        currentCard[''], #creator
                        currentCard[''], #creator id
                        currentCard[''], #created
                        currentCard[''], #updated
                        currentCard[''], #last viewed
                        currentCard[''], #resolved
                        currentCard[''], #affects version
                        currentCard[''], #fix versions
                        currentCard[''], #fix versions
                        currentCard[''], #components
                        currentCard[''], #components
                        currentCard[''], #due date
                        currentCard[''], #votes
                        currentCard[''], #labels
                        currentCard[''], #labels
                        currentCard[''], #labels
                        currentCard[''], #description
                        currentCard[''], #environment
                        currentCard[''], #watchers
                        currentCard[''], #watchers
                        currentCard[''], #watchers
                        currentCard[''], #watchers
                        currentCard[''], #watchers
                        currentCard[''], #watchers
                        currentCard[''], #watchers
                        currentCard[''], #watchers id
                        currentCard[''], #watchers id
                        currentCard[''], #watchers id
                        currentCard[''], #watchers id
                        currentCard[''], #watchers id
                        currentCard[''], #watchers id
                        currentCard[''], #watchers id
                        currentCard[''], #original estimate
                        currentCard[''], #remaining estimate
                        currentCard[''], #time spent
                        currentCard[''], #work ratio
                        currentCard[''], #Sum original estimate
                        currentCard[''], #sum remaining estimate
                        currentCard[''], #sum time spent
                        currentCard[''], #security level
                        currentCard[''], #outward issue link(blocks)
                        currentCard[''], #outward issue link(blocks)
                        currentCard[''], #outward issue link(blocks)
                        currentCard[''], #outward issue link(blocks)
                        currentCard[''], #outward issue link(blocks)
                        currentCard[''], #outward issue link(blocks)
                        currentCard[''], #outward issue link(blocks)
                        currentCard[''], #outward issue link(blocks)
                        currentCard[''], #outward issue link(blocks)
                        currentCard[''], #outward issue link(cloner)
                        currentCard[''], #outward issue link(duplicate)
                        currentCard[''], #outward issue link(issue split)







