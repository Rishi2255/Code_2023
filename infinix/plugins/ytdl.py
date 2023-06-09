import asyncio

import math

import os

import time

from .. import bot

from telethon import events

from telethon.tl.types import DocumentAttributeAudio

from yt_dlp import YoutubeDL

from yt_dlp.utils import (

    ContentTooShortError,

    DownloadError,

    ExtractorError,

    GeoRestrictedError,

    MaxDownloadsReached,

    PostProcessingError,

    UnavailableVideoError,

    XAttrMetadataError,

)

@bot.on(events.NewMessage(incoming=True, pattern="/yt ?(.*)"))

async def download_video(event):

  url = None

  t_type = None

  typee = str(event.pattern_match.group(1).lower())

  rl = typee.split(" ")

  url = rl[1]

  type = rl[0]

  

  

  await event.reply(url)

  vtx = await event.reply("`Preparing to download...`")

  if type == "a":

        opts = {

            "format": "bestaudio",

            "addmetadata": True,

            "key": "FFmpegMetadata",

            "writethumbnail": True,

            "prefer_ffmpeg": True,

            "geo_bypass": True,

            "nocheckcertificate": True,

            "postprocessors": [

                {

                    "key": "FFmpegExtractAudio",

                    "preferredcodec": "mp3",

                    "preferredquality": "480",

                }

            ],

            "outtmpl": "%(id)s.mp3",

            "quiet": True,

            "logtostderr": False,

        }

        video = False

        song = True

        

  elif type == "v": 

        opts = {

            "format": "best",

            "addmetadata": True,

            "key": "FFmpegMetadata",

            "prefer_ffmpeg": True,

            "geo_bypass": True,

            "nocheckcertificate": True,

            "postprocessors": [

                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}

            ],

            "outtmpl": "%(id)s.mp4",

            "logtostderr": False,

            "quiet": True,

        }

        song = False

        video = True

        

  try:

      await vtx.edit("Fetching data, please wait..")

      with YoutubeDL(opts) as ytdl:

        ytdl_data = ytdl.extract_info(url)

        

  except DownloadError as DE:

      await vtx.edit(f"{str(DE)}")

      return

  except ContentTooShortError:

      await vtx.edit("`The download content was too short.`")

      return

  except GeoRestrictedError:

      await vtx.edit(

            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"

        )

      return

  except MaxDownloadsReached:

      await vtx.edit("`Max-downloads limit has been reached.`")

      return

  except PostProcessingError:

      await vtx.edit("`There was an error during post processing.`")

      return

  except UnavailableVideoError:

      await vtx.edit("`Media is not available in the requested format.`")

      return

  except XAttrMetadataError as XAME:

      await vtx.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")

      return

  except ExtractorError:

      await vtx.edit("`There was an error during info extraction.`")

      return

  except Exception as e:

      await vtx.edit(f"{str(type(e)): {str(e)}}")

      return

  

      

  c_time = time.time()

  if song:

      await vtx.edit(

          f" `Preparing to upload song:`\

      \n**{ytdl_data['title']}**\

      \nby *{ytdl_data['uploader']}*"

      )

      await bot.send_file(

          event.chat_id,

          f"{ytdl_data['id']}.mp3",

          supports_streaming=True,

          attributes=[

              DocumentAttributeAudio(

                  duration=int(ytdl_data["duration"]),

                  title=str(ytdl_data['title']),

                  performer=str(ytdl_data["uploader"]),

              )   

          ],

          progress_callback=lambda d, t: asyncio.get_event_loop().create_task(

            progress(

                d, t, event, c_time, "uploading..", f"{ytdl_data['title']}.mp3"

            )

         ),

      )

      os.remove(f"{ytdl_data['id']}.mp3")      

        
