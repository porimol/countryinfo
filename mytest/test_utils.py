from os import listdir
from os.path import exists, join, isfile, getsize
import sys
import json 
import pycountry
from time import sleep

sys.path.insert(0, './../countryinfo')
from countryinfo import CountryInfo

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.distance import great_circle

## https://www.iso.org/obp/ui/#search inidcates there are 249 officially assigned 
## note that there are also:
## Exceptionally reserved: 13
## Transitionally reserved: 7
## Indeterminately reserved: 30
## Formerly used: 22
## Unassigne 335

country_nbr = len( pycountry.countries )
print( f"testing {len( pycountry.countries)} officially assigned codes" \
       f"Please check that number is correct at "\
       f"https://www.iso.org/obp/ui/#search" )


country_file_dir = '../countryinfo/data' 

def country_info_file_from_name( country_name ):
  if country_name is None :
    return None
  for file_name in listdir( country_file_dir ) :
    file_path = join( country_file_dir, file_name )
    if isfile(file_path) and 'json' in file_name :
      try: 
        with open( file_path, 'rt', encoding='utf-8') as f:
          country_info = json.load( f )
          if 'name' in country_info.keys() :
            if country_info[ 'name' ] is not None:
              if country_name.lower()  == country_info[ 'name' ].lower() :
                return file_path
          if 'altSpellings' in country_info.keys() :
            if country_name in country_info[ 'altSpellings' ] :
              return file_path
          if 'ISO' in country_info.keys() :
            if 'alpha2' in country_info[ 'ISO' ].keys() :
              if  country_name == country_info[ 'ISO' ][ 'alpha2' ] :
                return file_path
            if 'alpha3' in country_info[ 'ISO' ].keys() :
              if  country_name == country_info[ 'ISO' ][ 'alpha3' ] :
                return file_path
      except Exception as e:
        print( f" unable to load {file_path}" )
        raise ValueError(e)
  return None


def load_country_info_from_file( file_path ):
  """ load the object under file_payj """
  if exists( file_path ) :   
    if getsize( file_path ) > 0:
      with open( file_path, 'rt', encoding='utf-8') as f:
        country_info = json.load( f )
    else:
#      print( f"{file_path}: is void and can be removed" )
      country_info = {}
  else:
    country_info = {}
  return country_info

def file_name_from_country_name( country_name ):
  """ create a file name from a country_name """
  file_name = f"{country_name.lower()}"
  file_name = file_name.replace(' ', '_' ) 
  file_name = file_name.replace(',', '' ) 
  file_name = file_name.replace('.', '' ) 
  file_name = file_name.replace('(', '' ) 
  file_name = file_name.replace(')', '' ) 
  file_name = file_name.replace('.', '' ) 
  file_name = f"{file_name}.json"
  return file_name


def all_country( dry_run=True ):
  """ ensure CoutnryInfo can be instantiated from iso2, iso3, name, official_name
 
  These information has provided by pycountry
  
  Args:
    dry_run (bool): must be set to False to changes to be enforced. 
      Set to True by default.

  """
  for country in list(pycountry.countries):
    iso2 = country.alpha_2
    iso3 = country.alpha_3
    name = country.name
    try:
      official_name = country.official_name
    except AttributeError:
      official_name = None
    if official_name is None:
      designation_list = [ iso2, iso3, name ]
    else: 
      designation_list = [ iso2, iso3, name, official_name ]
    try: 
      for designation in designation_list :
        country = CountryInfo( designation )
        country.info()
    except Exception as e:
      print( f"{e.__class__} : unable to instantiate CountryInfo from one "\
             f"or more of the following keys: {designation_list}" )
      ## try to get the file from name
      file_path = country_info_file_from_name( name ) 
      if file_path is None:
        file_path = country_info_file_from_name( official_name )
        if file_path is None:
          file_path = country_info_file_from_name( iso2 )
          if file_path is None:
            file_path = country_info_file_from_name( iso3 )
            if file_path == None:
              file_name = file_name_from_country_name( name ) 
              print( f"creating a new file {file_name}" )
              file_path = join( country_file_dir, f"{file_name}" )
      country_info = load_country_info_from_file( file_path )
      iso_dict = { 'alpha2' : iso2, 'alpha3' : iso3 }
      if 'ISO' not in country_info.keys() :
        print( f"{file_path}: 'ISO' key not found -> "\
               f" creating country_info[ 'ISO' ] = {iso_dict}" ) 
        country_info[ 'ISO' ] = iso_dict
      elif country_info[ 'ISO' ] != iso_dict :
          print( f"{file_path}: found {country_info[ 'ISO' ]} / "\
                 f"expected {iso_dict} -> overwriting country_info[ 'ISO' ]" ) 
          country_info[ 'ISO' ] = iso_dict
      ## checking name
      if 'name' not in country_info.keys() :
        print( f"{file_path}: 'name' key not found -> creating "\
               f"country_info[ 'name' ] = {name}" ) 
        country_info[ 'name' ] = name
      elif country_info[ 'name' ] in [ None, '' ] :
        print( f"{file_path}: empty 'name' -> overwriting "\
               f"country_info[ 'name' ] = {name}" ) 
      ## Ensure name, official_name, iso are either in name or altSpellings
      for designation in designation_list :
        if designation == country_info[ 'name' ] :
          continue
        if 'altSpellings' not in country_info.keys() :
          print( f"{file_path}: 'altSpellings' key not found -> creating "\
                 f"country_info[ 'altSpellings' ] = [ {designation} ]" ) 
          country_info[ 'altSpellings' ] = [ designation ]
        elif designation not in country_info[ 'altSpellings' ] :
          print( f"{file_path}: {designation} not found in 'altSpellings' -> "\
                 f"adding {designation}" ) 
          country_info[ 'altSpellings' ].append( designation )
      if dry_run is False :
        confirmation = input( 'Confirm overwriting : y /[n]' )
        if confirmation == 'y':
          with open( file_path, 'wt', encoding='utf-8') as f:
            json.dump( country_info, f, indent=2 )

def check_alt_designation( name_transformed=False ):
  """ ensures country lists used by ICANN enables a countryInfo lookup

  """

  with open( 'country_list_u.txt', 'rt', encoding='utf8' ) as f:
    for country_name in f.readlines():
      if name_transformed is True:
        country_name = country_name.strip( )
        ## it seems that (Republic of) is also used instead of the official ", Republic of" 
        if ' (' in country_name.lower() and ')' in country_name.lower():
          country_name = country_name.replace( ' (', ', ' )
          country_name = country_name.replace( ')', '' )
        if 'ivoire' in country_name.lower() :
          country_name = "C\u00f4te d'Ivoire"
        elif country_name.lower() == 'curacao' :
          country_name = "Curaçao"
        elif 'holy see' in country_name.lower() or \
             'vatican' in country_name.lower():
          country_name = "Holy See (Vatican City State)"
        elif 'hong kong' in country_name.lower():
          country_name = "Hong Kong"
        ## korea is usually understood as replublic of korea
        elif country_name.lower().strip() == 'korea' :
#          ( 'korea' in country_name.lower() and 'republic' in country_name.lower()) :
          country_name = "Republic of Korea"
        elif 'northern' in country_name.lower() and 'ireland' in country_name.lower() :
          country_name = "United Kingdom of Great Britain and Northern Ireland"
      try: 
        country = CountryInfo( country_name.strip() )
        country.iso( )
#        country.info()
      except Exception as e:
        print( f"Cannot find countryInfo for {country_name}" )

def detect_empty_and_unexpected_files( ):
  for file_name in listdir( country_file_dir ) :
    file_path = join( country_file_dir, file_name )
    if getsize( file_path ) == 0:
      print( f"{file_name}: Empty file" )
      continue
    try: 
      country_info = load_country_info_from_file( file_path )
    except Exception as e:
      print( f"{file_name} unable to load file." ) 
      
    for k in [ 'ISO', 'altSpellings', 'name' ] :
      if k not in country_info.keys():
        print( f"{file_path} : unexpected format no key {k} -- {country_info}" )

def detecting_double_and_void_files( ):
  """check files that are emtpy or that share (at least one) iso code

  file with NO iso codes are ignored.
  """

  for file_name in listdir( country_file_dir ) :
    if '.json' not in file_name:
      continue
    file_path = join( country_file_dir, file_name )
    if getsize( file_path ) == 0:
      print( f"Empty file {file_name}" )
      continue
    try: 
      country_info = load_country_info_from_file( file_path )
    except Exception as e:
      print( f"{file_path} : unable to load country_info" )
      continue
    
    try: 
      iso2 = country_info[ 'ISO' ][ 'alpha2' ]
    except KeyError:
      iso2 = None
    try: 
      iso3 = country_info[ 'ISO' ][ 'alpha3' ]
    except KeyError:
      iso3 = None
    if iso2 is None and iso3 is None:
      continue
    for file_name_bis in listdir( country_file_dir ) :
      if file_name_bis == file_name :
        continue
      if '.json' not in file_name_bis:
        continue
      file_path_bis = join( country_file_dir, file_name_bis )
      try:
        country_info_bis = load_country_info_from_file( file_path_bis )
      except Exception as e:
        print( f"{file_path_bis} : unable to load country_info" )
        continue
      try: 
        iso2_bis = country_info_bis[ 'ISO' ][ 'alpha2' ]
      except KeyError:
        iso2_bis = None
      try: 
        iso3_bis = country_info_bis[ 'ISO' ][ 'alpha3' ]
      except KeyError:
        iso3_bis = None
      iso_bis = country_info_bis[ 'ISO' ][ 'alpha2' ]
      if iso2_bis is None and iso3_bis is None:
        continue
      if iso2_bis == iso2 or iso3_bis == iso3 :
        print( f"Check duplication:  {file_name} and {file_name_bis}" )


def proposed_value( country_info, key, proposed_value, dry_run=True, file_path=""):
  """ check the presence of proposed_value under key

  If the key does not exist or value is empty, creates country_info[ key ] = proposed_value.
  If current value and proposed values are different propose to keep or replace the current value.
  """
  if key in country_info.keys() :
    if country_info[ key ] not in [ "", None ] and\
       country_info[ key ] != proposed_value :
      txt = f"{file_path} : {country_info[ 'name' ]} : different value found for {key}-> "\
            f"replacing {country_info[ key ]} by {proposed_value} ? y/n"
      if dry_run is False :
        
        confirmation = input( txt )
        if confirmation == 'y':
          country_info[ key ] = proposed_value
      else:
        print( txt )
  else: 
    txt = f"{file_path} : {country_info[ 'name' ]} :  {key} not found or empty value  -> adding "\
          f"country_info[ {key} ] = {proposed_value} ? y/n"
    if dry_run is False :
      confirmation = input( txt )
      if confirmation == 'y':
        country_info[ key ] = proposed_value
    print( txt )
    country_info[ key ] = proposed_value
  return country_info

def most_capital( dry_run=True):
  """ checking capitals and latlong
  
  when capital is missing we can use the following file:
    https://gist.github.com/pamelafox/986163

  """
  with open( 'pamelafox_country_info.json', 'rt', encoding='utf-8') as f:
    country_list = json.load( f )
  for country in country_list:
    name = country[ 'name' ]
    iso2 = country[ 'code' ]
    capital = country[ 'capital' ]
    region = country[ 'continent' ]
    file_path = country_info_file_from_name( iso2 )
    if file_path is None:
      file_path = country_info_file_from_name( name )
      file_name = file_name_from_country_name( country_name ) 
      print( f"creating a new file {file_name}" )
      file_path = join( country_file_dir, f"{file_name}" )
      country_info = {}
    else:
      country_info = load_country_info_from_file( file_path )
   
    if 'name' in country_info.keys() : 
      if country_info[ 'name' ] in [ None, "" ] :
        print( f"{file_path}: empty 'name' value -> creating "\
               f"country_info[ 'name' ] = {name}" )
        country_info[ 'name' ] = name
    else:
      print( f"{file_path}: 'name' key not found -> creating "\
             f"country_info[ 'name' ] = {name}" )
      country_info[ 'name' ] = name
    ## check name is eithe rin name or altSpellings
    designation_list = [ name ]
    if 'altSpellings' in country_info.keys() :
      designation_list.extend( country_info[ 'altSpellings' ] )
    if name not in designation_list :
      if 'altSpellings' in country_info.keys() :
        print( f"{file_path}: unknown designation {name} -> "\
               f"adding {name} to country_info[ 'altSpellings' ]" )
        country_info[ 'altSpellings' ].append( name )
      else:
        print( f"{file_path}: unknown designation {name} -> "\
               f"creating country_info[ 'altSpellings' ] = [ {name} ]" )
        country_info[ 'altSpellings' ] = [ name ]
    country_info = proposed_value( country_info, 'capital', capital, dry_run=dry_run)
    if 'region' in country_info.keys():
      if country_info[ 'region' ] == 'Americas' :
        country_info = proposed_value( country_info, 'subregion', region, dry_run=dry_run )
    else:
      country_info = proposed_value( country_info, 'region', region, dry_run=dry_run )

    if dry_run is False :
      confirmation = input( 'Confirm overwriting : y /[n]' )
      if confirmation == 'y':
        with open( file_path, 'wt', encoding='utf-8') as f:
          json.dump( country_info, f, indent=2 )
                     

sleep_time = 1


def nominatim_capital_latgln_translations(  dry_run=True ):
  """
  Check / and fill with captial latitude coordinates

  It is expected that name and capital are provided
  """
  skip = True
  geolocator = Nominatim( user_agent='country_info' )
  for file_name in listdir( country_file_dir ) :
    print( file_name )
    file_path = join( country_file_dir, file_name )
    if isfile(file_path) and file_name[-5:] == '.json':
      with open( file_path, 'rt', encoding='utf-8') as f:
        country_info = json.load( f )
    else:
      continue
    
#    if skip is True:
#      if file_name == "netherlands_antilles.json":
#        skip = False
#      continue
    
    key_list = country_info.keys()
    confirmation = None
    if 'name' not in  key_list :
      print( f"ERROR: {file_path} : no name found for {country_info}.")
      if dry_run is True:
        continue
      else:
        name = input( f"Enter the name" )
        country_info = proposed_value( country_info, 'name', name, dry_run=dry_run,\
                       file_path=file_path)
    if 'capital' not in key_list:
      print( f"ERROR: {file_path} : no capital found for {country_info}.")
      if dry_run is True:
        continue
      else:
        capital = input( f"Enter the english capital name" )
        country_info = proposed_value( country_info, 'capital', capital, dry_run=dry_run,\
                       file_path=file_path)
      
    if 'capital_latlng' not in key_list :
      country_info[ 'capital_latlng' ] = []
    name = country_info[ 'name' ]
    capital = country_info[ 'capital' ]
    capital_latlng = country_info[ 'capital_latlng' ]
    iso2 = country_info[ 'ISO' ] [ 'alpha2' ]
    search_string = f"{name} {capital}"
    try:
      geo_capital, geo_capital_latlng = geolocator.geocode( search_string )
      sleep(sleep_time)
    except: 
      print( f"ERROR: {file_path} : Unsuccessful Nominatim search  {search_string}" )
      continue
      ## native
    reverse = geolocator.reverse( geo_capital_latlng )
    geo_country = reverse.raw[ 'address' ][ 'country' ]
    geo_iso2 = reverse.raw[ 'address' ][ 'country_code' ]
    sleep(sleep_time)
    ## en
    try: 
      reverse = geolocator.reverse( geo_capital_latlng, language='en')
      en_geo_city = reverse.raw[ 'address' ][ 'city' ]
      en_geo_country = reverse.raw[ 'address' ][ 'country' ]
      sleep(sleep_time)
    except: 
      print( f"ERROR: {file_path} : Unsuccessful Nominatim reverse for {geo_capital_latlng}" )
      continue

    translations = {}
    ## de
    reverse = geolocator.reverse( geo_capital_latlng, language='de')
    translations[ 'de' ] = reverse.raw[ 'address' ][ 'country' ]
    sleep(sleep_time)
    ## es
    reverse = geolocator.reverse( geo_capital_latlng, language='es')
    translations[ 'es' ] = reverse.raw[ 'address' ][ 'country' ]
    sleep(sleep_time)
    ## fr
    reverse = geolocator.reverse( geo_capital_latlng, language='fr')
    translations[ 'fr' ] = reverse.raw[ 'address' ][ 'country' ]
    sleep(sleep_time)
    ## ja
    reverse = geolocator.reverse( geo_capital_latlng, language='ja')
    translations[ 'ja' ] = reverse.raw[ 'address' ][ 'country' ]
    sleep(sleep_time)
    ## it
    reverse = geolocator.reverse( geo_capital_latlng, language='it')
    translations[ 'it' ] = reverse.raw[ 'address' ][ 'country' ]
    sleep(sleep_time)
    if geo_iso2.lower() != iso2.lower() :
      print( f"ERROR: {file_path} : {name} {en_geo_country} : iso2 mismatch "\
             f"between country_info ({iso2}) and Geo {geo_iso2})" )
      continue
    if 'altSpellings' not in country_info.keys() :
      country_info[ 'altSpellings' ] = []
    if en_geo_country != name and en_geo_country not in country_info[ 'altSpellings' ]:
      txt = f"{file_path} : adding country name {en_geo_country} to 'altSpellings' ?"
      if dry_run is True:
        print( txt )
      else: 
        confirmation = input( txt )
        if confirmation == 'y':
          country_info[ 'altSpellings' ].append( en_geo_country )
#    try: 
#      native_name = country_info[ 'nativeName' ]
#    except KeyError:
#      native_name = None
#      country_info[ 'nativeName' ] = native_name
#    if geo_country !=  native_name:
#      print( f"{file_path} : replacing nativeName {native_name} by {geo_country} ?" )
    country_info = proposed_value( country_info, 'nativeName', geo_country, dry_run=dry_run)
      
##    if en_geo_city != capital:
##      print( f"{file_path} : replacing capital name {capital} by {en_geo_city} ?" )
    country_info = proposed_value( country_info, 'capital', en_geo_city, dry_run=dry_run)

    distance = geodesic( capital_latlng, geo_capital_latlng ).km
    if distance > 10 :
      print( f"{file_path} : replacing capital latlng {capital_latlng} "\
             f"by {geo_capital_latlng} - {distance} Km?" )
      country_info = proposed_value( country_info, 'capital_latlng', geo_capital_latlng, dry_run=dry_run)
    if 'translations' not in country_info.keys() :
      country_info[ 'translations' ] = {}
    for k in [ 'de', 'es', 'fr', 'ja', 'it' ]:
      if k not in country_info[ 'translations' ].keys():
        txt = f"{file_path} : no translation found for {k} -> setting to {translations[ k ]} y/n?"
        if dry_run is True:
          print( txt )
        else :
          confirmation = input( txt )
          if confirmation == 'y':
            country_info[ 'translations' ][ k ] = translations[ k ]
      elif country_info[ 'translations' ][ k ] != translations[ k ]:
        txt = f"{file_path} : current translation for {k} : {country_info[ 'translations' ][ k ]} -> replacing with {translations[ k ]} y/n?"
        if dry_run is True:
          print( txt )
        else :
          confirmation = input( txt )
          if confirmation == 'y':
            country_info[ 'translations' ][ k ] = translations[ k ]
    if dry_run is False :
      confirmation = input( 'Confirm overwriting : y /[n]' )
      if confirmation == 'y':
        with open( file_path, 'wt', encoding='utf-8') as f:
          json.dump( country_info, f, indent=2 )
        

def has_capital_and_latlng( ): 
  geolocator = Nominatim( user_agent='country_info' )
  for file_name in listdir( country_file_dir ) :
    file_path = join( country_file_dir, file_name )
    if isfile(file_path) and file_name[-5:] == '.json':
      try:
        with open( file_path, 'rt', encoding='utf-8') as f:
          country_info = json.load( f )
      except:
         print( f"ERROR: unable to open {file_name}" )
    else:
      continue
    for k in [ 'name', 'capital', 'capital_latlng' ]:
      if k not in country_info.keys() :
        print( f"{file_name} has no {k}" )
    if 'capital' not in country_info.keys() or \
       'capital_latlng' not in country_info.keys() or \
       'name' not in country_info.keys():
      continue
    name = country_info[ 'name' ]
    capital = country_info[ 'capital' ]
    capital_latlng = country_info[ 'capital_latlng' ]
    search_string = f"{name} {capital}"
    if capital is None or capital_latlng is None:
      print( f"{file_name} : {name} has its capital {capital} {capital_latlng}" )
      continue 
    continue
    try: 
      geo_capital, geo_capital_latlng = geolocator.geocode( search_string )
    except:
      print( f"{file_name} : Nominatim unable to find location for {search_string}" )
     

    if isinstance( capital_latlng[ 0 ], list ):
      distance = []
      for latlng  in capital_latlng:
        distance.append( geodesic( latlng, geo_capital_latlng ).km )
#      print( f"{file_name} : Nominatim( {name} - {capital} ) is {geo_capital} "\
#             f"located a {distance} from country_info[ 'capital_latlng' ]" )   
        
    elif isinstance( capital_latlng[ 0 ], float) :
      distance = geodesic( capital_latlng, geo_capital_latlng ).km
#      if distance > 10 :
#        print( f"{file_name} : Nominatim( {name} - {capital} ) is {geo_capital} "\
#               f"located a {distance} from country_info[ 'capital_latlng' ]" )   
    
    else: 
      print( f"{file_name} : unexpected format for {name} has its capital "\
             f"{capital} {capital_latlng}" )


def check_region( dry_run=True ):
  ## this section considers the list of regions, subregions and intermediate-region.

  ## Information is taken from 
  ##https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes
  ## designation seems mor ein line with UN M49
  ## https://unstats.un.org/unsd/methodology/m49/
  ## building region/subregion list
  file_path = '/home/emigdan/gitlab/ISO-3166-Countries-with-Regional-Codes/all/all.json'
  try:
    with open( file_path, 'rt', encoding='utf-8') as f:
      region_list = json.load( f )
  except:
    print( f"ERROR: unable to open {file_path}" )

  for file_name in listdir( country_file_dir ) :
    file_path = join( country_file_dir, file_name )
    if isfile(file_path) and file_name[-5:] == '.json':
      try:
        with open( file_path, 'rt', encoding='utf-8') as f:
          country_info = json.load( f )
          try:
            region = country_info[ 'region' ]
          except KeyError:
            region = None
          try:
            subregion = country_info[ 'subregion' ]
            ## adjustment
            if subregion == 'South-Eastern Asia':
              subregion = 'South-eastern Asia'
          except KeyError:
            subregion = None
          alpha2 = country_info[ 'ISO' ][ 'alpha2' ]
      except:
         print( f"ERROR: unable to open {file_name}" )
    else:
      continue
    ref_region = None
    ## historic country code are not considered in all
    ## the question remain on whether to consider thes ecountry codes or not.
    if alpha2 == 'AN':
      alpha2_match = 'BQ'
    else:
      alpha2_match = alpha2
    for r in region_list:
      if r[ 'alpha-2' ] == alpha2_match :
        ref_region = r
      
    if ref_region is None:
      print( f"ERROR: {alpha2}: unable to find country {alpha2} in region list for country_info {alpha2} [{file_name}]" )

    if region != None and region != ref_region[ 'region' ]:
      print( f"ERROR: {alpha2}: country_info region {region} mismatch value from region_list {ref_region[ 'region' ]}" )
    if subregion != None and subregion != ref_region[ 'sub-region' ]:
      print( f"ERROR: {alpha2}: country_info region {subregion} mismatch value from region_list {ref_region[ 'sub-region' ]}" )

    if dry_run is False :
      country_info[ 'region' ] = ref_region[ 'region' ]
      country_info[ 'subregion' ] = ref_region[ 'sub-region' ]
      country_info[ 'intermediateregion' ] = ref_region[ 'intermediate-region' ]
    else:
      print( f"replacing {alpha2} ")
      print( f"  - region: {region}" )
      print( f"  - subregion: {subregion}" )
      print( f"by:" )
      print( f"  - region: {ref_region[ 'region' ]}" )
      print( f"  - sub-region: {ref_region[ 'sub-region' ]}" )
      print( f"  - intermediary: {ref_region[ 'intermediate-region' ]}" )
      country_info[ 'region' ] = ref_region[ 'region' ]
      country_info[ 'subregion' ] = ref_region[ 'sub-region' ]
      country_info[ 'intermediateregion' ] = ref_region[ 'intermediate-region' ]
      confirmation = input( 'Confirm overwriting : y /[n]' )
      if confirmation == 'y':
        with open( file_path, 'wt', encoding='utf-8') as f:
          json.dump( country_info, f, indent=2 )
        
#| name                                 |  ISO2 | capital/capital_lat_lgn | Comment 
#|--------------------------------------|-------|-------------------------|----------
#|United States Minor Outlying Islands | UM    | None / None             | redirect to Honolulu
#|Bonaire, Sint Eustatius and Saba     | BQ    | 3 cities                | Kralendijk [ 12.144444, -68.265556 ] the largest city
#|Bouvet Island                        | BV    | None / None             | uninhabited
#|Antartica                            | AQ    | None / None             | (almost) uninhabited
#|Heard Island and McDonald Islands    | HM    | None / None             | uninhabited

## Check all countries have an entry with name and country code. 
## All countries can be instantiated with name, country codes
## all_country( dry_run=True)
## Check designation used by ICANN are included
# check_alt_designation( name_transformed=True )
## Detection of empty or unexpected files
#detect_empty_and_unexpected_files( )
## Check duplicated files /empty files
# detecting_double_and_void_files( )
## check most countries have there capital filled
## most_capital( dry_run=True)
## check every country_info entry have a capital and associated latitude longitude
## and check the value is appropriated.
#nominatim_capital_latgln_translations(  dry_run=False )
## has_capital_and_latlng()
check_region( dry_run=True )

