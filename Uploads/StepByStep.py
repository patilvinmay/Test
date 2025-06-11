import os, shutil
import HeadlessBrowsing as hb
import MakingChunks as ck
import RemoveSearchEchoes as rse

# Cleanup previous data from folders
hb.empty_directory("chunks")
hb.empty_directory("LogsAndData")
hb.empty_directory("RuntimeScreenShots")

# First search the Merchant on Bing and take screenshot
merchant_query = "10001_ET 415 W SOLOMAN ST GRIFFIN GA"
search_result_ss_path = hb.search_bing(merchant_query)

# Second make chunks of screenshot
output_dir = "chunks"
chunks = ck.process_image_remove_header_and_split(search_result_ss_path, output_dir)

# Third search for Search echoes
search_echo_flag = rse.ocr_plus_fuzzy(chunks[2])
# search_echo_flag = rse.ocr_plus_fuzzy("chunks\\left_links_cleaned.png")
