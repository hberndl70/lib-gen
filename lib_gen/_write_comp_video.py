import sys, os
from lxml import etree
from lib_gen import  _edx_consts
import __SETTINGS__

#--------------------------------------------------------------------------------------------------
ALL_LANGUAGES = {'en': 'English'} 

#--------------------------------------------------------------------------------------------------
# Text Strings
WARNING       = "      WARNING:"

#--------------------------------------------------------------------------------------------------
# write xml for video component
def writeXmlForVidComp(component_path, filename, settings, unit_filename):

    # ----  ----  ----
    # Youtube Video
    # <video 
    #   url_name="section_week_1_subsection_2_shorts_unit_1_text_and_videos_02_video" 
    #   sub="" 
    #   transcripts="{&quot;en&quot;: &quot;7d76f250-0000-42ea-8aba-c0c0ce845280-en.srt&quot;}" 
    #   display_name="A Video" edx_video_id="7d76f250-0000-42ea-8aba-c0c0ce845280" 
    #   youtube_id_1_0="3_yD_cEKoCk" >
    #
    #   <video_asset client_video_id="External Video" duration="0.0" image="">
    #     <transcripts>
    #       <transcript file_format="srt" language_code="en" provider="Custom"/>
    #     </transcripts>
    #   </video_asset>
    #   <transcript language="en" src="7d76f250-0000-42ea-8aba-c0c0ce845280-en.srt"/>
    # </video>
    # ----  ----  ----

    # ----  ----  ----
    # Non-Youtube video
    # <video 
    #   url_name="section_week_1_subsection_2_shorts_unit_1_text_and_videos_02_video" 
    #   sub="" 
    #   transcripts="{&quot;en&quot;: &quot;7d76f250-0000-42ea-8aba-c0c0ce845280-en.srt&quot;}" 
    #   display_name="A Video" edx_video_id="7d76f250-0000-42ea-8aba-c0c0ce845280" 
    #   html5_sources="[&quot;https://aaa.bbb.com/ccc.mp4&quot;]"  >
    #
    #   <video_asset client_video_id="External Video" duration="0.0" image="">
    #     <transcripts>
    #       <transcript file_format="srt" language_code="en" provider="Custom"/>
    #     </transcripts>
    #   </video_asset>
    #   <transcript language="en" src="7d76f250-0000-42ea-8aba-c0c0ce845280-en.srt"/>
    # </video>
    # ----  ----  ----

    # create xml
    video_tag = etree.Element("video")
    video_tag.set('url_name', filename)
    for key in settings:
        if key not in ['type', 'transcript', 'title', 'video_filename']:
            video_tag.set(key, settings[key])

    # check we have either youtube_id_1_0 or video
    if not 'youtube_id_1_0' in settings and not 'video_filename' in settings:
        print(WARNING, 'A video component must have either a "youtube_id_1_0" setting or a "video" setting:', unit_filename)

    # add youtube
    if 'youtube_id_1_0' in settings:
        video_tag.set('youtube', '1.00:' + settings['youtube_id_1_0'])
    else:
        video_tag.set('youtube_id_1_0', '')

    # add the video asset tag
    video_asset_tag = etree.Element("video_asset")
    video_asset_tag.set('client_video_id', 'external video')
    video_asset_tag.set('duration', '0.0')
    video_asset_tag.set('image', '')
    video_tag.append(video_asset_tag)

    video_urls = {}

    # if mp4, then create xml
    if 'video_filename' in settings:
        video_urls = addVideoXML(video_tag, video_asset_tag, component_path, settings, unit_filename)
        
    # write XML file to COMP_VIDS_FOLDER
    video_data = etree.tostring(video_tag, pretty_print = True)
    video_xml_out_path = os.path.join(sys.argv[2], _edx_consts.COMP_VIDS_FOLDER, filename + '.xml')
    with open(video_xml_out_path, 'wb') as fout:
        fout.write(video_data)

    # creat a list of files to return
    files = [
        [filename, _edx_consts.COMP_VIDS_FOLDER]
    ]

    # return the file name and folder
    return files

#--------------------------------------------------------------------------------------------------
# xml for the video
def addVideoXML(video_tag, video_asset_tag, component_path, settings, unit_filename):
    video_urls = {}

    # get the filename
    video_filename_ext = settings['video_filename'].strip()
    [video_filename, video_ext] = video_filename_ext.split('.')

    # the dir of this component
    component_dir = os.path.dirname(component_path)


    # for example "https://sos-de-fra-1.exo.io/exoscale-academy/videos/video_file.mp4"
    # create the video urls
    
    url_base = __SETTINGS__.S3_URL + __SETTINGS__.S3_BUCKET + '/' + __SETTINGS__.S3_FOLDER + '/'

    for lang in __SETTINGS__.LANGUAGES:
        video_urls[lang] = url_base  + video_filename + '.' + video_ext

    video_url_default = video_urls['en']
    if video_url_default == None:
        video_url_default = video_urls[video_urls.keys()[0]]

 
    # set the html5_sources
    # html5_sources="[&quot;https://sos-de-fra-1.exo.io/exoscale-academy/videos/video_file.mp4&quot;]"
    video_tag.set('html5_sources', '["' + video_url_default + '"]')

    # add the source tag
    source_tag = etree.Element("source")
    source_tag.set('src', video_url_default)
    video_tag.append(source_tag)

    # return the urls
    return video_urls

#--------------------------------------------------------------------------------------------------
