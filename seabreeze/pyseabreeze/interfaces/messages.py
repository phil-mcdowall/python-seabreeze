
class OBPMessage(object):
    # Generic Device Commands
    RESET = 0x00000000
    RESET_DEFAULTS = 0x00000001
    GET_HARDWARE_REVISION = 0x00000080
    GET_FIRMWARE_REVISION = 0x00000090
    GET_SERIAL_NUMBER = 0x00000100
    GET_DEVICE_ALIAS = 0x00000200
    GET_DEVICE_ALIAS_LENGTH = 0x00000201
    SET_DEVICE_ALIAS = 0x00000210
    GET_NUMBER_USER_STRINGS = 0x00000300
    GET_USER_STRING_LENGTH = 0x00000301
    GET_USER_STRING = 0x00000302
    SET_USER_STRING = 0x00000310
    GET_RS232_BAUDRATE = 0x00000800
    GET_RS232_FLOW_CONTROL_MODE = 0x00000804
    SET_RS232_BAUDRATE = 0x00000810
    SET_RS232_FLOW_CONTROL_MODE = 0x00000814
    SAVE_RS232_SETTINGS = 0x000008F0
    CONFIGURE_STATUS_LED = 0x00001010
    REPROGRAMMING_MODE = 0x000FFF00
    # Spectrometer Commands
    GET_AND_SEND_CORRECTED_SPECTRUM = 0x00101000
    GET_AND_SEND_RAW_SPECTRUM = 0x00101100
    GET_PARTIAL_SPECTRUM_MODE = 0x00102000
    GET_AND_SEND_PARTIAL_CORRECTED_SPECTRUM = 0x00102080
    SET_INTEGRATION_TIME = 0x00110010
    SET_TRIGGER_MODE = 0x00110110
    SIMULATE_TRIGGER_PULSE = 0x00110120
    GET_PIXEL_BINNING_FACTOR = 0x00110280
    GET_MAXIMUM_BINNING_FACTOR = 0x00110281
    SET_BINNING_FACTOR = 0x00110290
    SET_DEFAULT_BINNING_FACTOR = 0x00110295
    SET_LAMP_ENABLE = 0x00110410
    SET_TRIGGER_DELAY = 0x00110510
    GET_SCANS_TO_AVERAGE = 0x00120000
    SET_SCANS_TO_AVERAGE = 0x00120010
    GET_BOXCAR_WIDTH = 0x00121000
    SET_BOXCAR_WIDTH = 0x00121010
    GET_WAVELENGTH_COEFFICIENT_COUNT = 0x00180100
    GET_WAVELENGTH_COEFFICIENT = 0x00180101
    SET_WAVELENGTH_COEFFICIENT = 0x00180111
    GET_NONLINEARITY_COEFFICIENT_COUNT = 0x00181100
    GET_NONLINEARITY_COEFFICIENT = 0x00181101
    SET_NONLINEARITY_COEFFICIENT = 0x00181111
    GET_IRRADIANCE_CALIBRATION = 0x00182001
    GET_IRRADIANCE_CALIBRATION_COUNT = 0x00182002
    GET_IRRADIANCE_CALIBRATION_COLLECTION_AREA = 0x00182003
    SET_IRRADIANCE_CALIBRATION = 0x00182011
    SET_IRRADIANCE_CALIBRATION_COLLECTION_AREA = 0x00182013
    GET_NUMBER_STRAY_LIGHT_COEFFICIENTS = 0x00183100
    GET_STRAY_LIGHT_COEFFICIENT = 0x00183101
    SET_STRAY_LIGHT_COEFFICIENT = 0x00183111
    GET_HOT_PIXEL_INDICES = 0x00186000
    SET_HOT_PIXEL_INDICES = 0x00186010
    GET_BENCH_ID = 0x001B0000
    GET_BENCH_SERIAL_NUMBER = 0x001B0100
    GET_SLIT_WIDTH_MICRONS = 0x001B0200
    GET_FIBER_DIAMETER_MICRONS = 0x001B0300
    GET_FILTER = 0x001B0500
    GET_COATING = 0x001B0600
    # GPIO commands
    GET_NUMBER_GPIO_PINS = 0x00200000
    GET_OUTPUT_ENABLE_VECTOR = 0x00200100
    SET_OUTPUT_ENABLE_VECTOR = 0x00200110
    GET_VALUE_VECTOR = 0x00200300
    SET_VALUE_VECTOR = 0x00200310
    # Strobe commands
    SET_SINGLE_STROBE_PULSE_DELAY = 0x00300010
    SET_SINGLE_STROBE_PULSE_WIDTH = 0x00300011
    SET_SINGLE_STROBE_ENABLE = 0x00300012
    SET_CONTINUOUS_STROBE_PERIOD = 0x00310010
    SET_CONTINUOUS_STROBE_ENABLE = 0x00310011
    # Temperature Commands
    GET_TEMPERATURE_SENSOR_COUNT = 0x00400000
    READ_TEMPERATURE_SENSOR = 0x00400001
    READ_ALL_TEMPERATURE_SENSORS = 0x00400002
