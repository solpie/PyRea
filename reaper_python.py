#coding=utf-8
import re
from ctypes import *

# lowercase rpr_ functions are for internal use

_ft = {}


def rpr_initft(ft):
    if (len(_ft) == 0):
        _ft.update(ft)


def rpr_getfp(fn):
    return _ft[fn]


def rpr_packp(t, v):
    m = re.match('^\((\w+\*)\)0x([0-9A-F]+)$', str(v))
    if (m != None):
        (_t, _v) = m.groups()
        if (_t == t or t == 'void*'):
            p = c_uint(int(_v, 16)).value
            if (RPR_ValidatePtr(p, t)):
                return p
    return 0


def rpr_unpackp(t, v):
    if (v == None):
        v = 0
    return '(%s)0x%08X' % (t, v)


def RPR_ValidatePtr(p, t):
    a = _ft['ValidatePtr']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p)(a)
    return f(c_uint(p), rpr_packsc(t))


def rpr_packsc(v):
    return c_char_p(str(v).encode())


def rpr_packs(v):
    MAX_STRBUF = 4 * 1024 * 1024
    return create_string_buffer(str(v).encode(), MAX_STRBUF)


def rpr_unpacks(v):
    return str(v.value.decode())


def RPR_GetAudioAccessorSamples(p0, p1, p2, p3, p4, p5):
    a = _ft['GetAudioAccessorSamples']
    f = CFUNCTYPE(c_int, c_uint, c_int, c_int, c_double, c_int, c_void_p)(a)
    v = cast((c_double * p2 * p4)(), POINTER(c_double))
    t = (rpr_packp('void*', p0), c_int(p1), c_int(p2), c_double(p3), c_int(p4), v)
    r = f(t[0], t[1], t[2], t[3], t[4], t[5])
    for i in range(p2 * p4):
        p5[i] = float(v[i])
    return (r, p5)


def RPR_AddMediaItemToTrack(p0):
    a = _ft['AddMediaItemToTrack']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return rpr_unpackp('MediaItem*', r)


def RPR_AddProjectMarker(p0, p1, p2, p3, p4, p5):
    a = _ft['AddProjectMarker']
    f = CFUNCTYPE(c_int, c_uint, c_byte, c_double, c_double, c_char_p, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), c_byte(p1), c_double(p2), c_double(p3), rpr_packsc(p4), c_int(p5))
    r = f(t[0], t[1], t[2], t[3], t[4], t[5])
    return r


def RPR_AddProjectMarker2(p0, p1, p2, p3, p4, p5, p6):
    a = _ft['AddProjectMarker2']
    f = CFUNCTYPE(c_int, c_uint, c_byte, c_double, c_double, c_char_p, c_int, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), c_byte(p1), c_double(p2), c_double(p3), rpr_packsc(p4), c_int(p5), c_int(p6))
    r = f(t[0], t[1], t[2], t[3], t[4], t[5], t[6])
    return r


def RPR_AddTakeToMediaItem(p0):
    a = _ft['AddTakeToMediaItem']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('MediaItem*', p0),)
    r = f(t[0])
    return rpr_unpackp('MediaItem_Take*', r)


def RPR_adjustZoom(p0, p1, p2, p3):
    a = _ft['adjustZoom']
    f = CFUNCTYPE(None, c_double, c_int, c_byte, c_int)(a)
    t = (c_double(p0), c_int(p1), c_byte(p2), c_int(p3))
    f(t[0], t[1], t[2], t[3])


def RPR_AnyTrackSolo(p0):
    a = _ft['AnyTrackSolo']
    f = CFUNCTYPE(c_byte, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    r = f(t[0])
    return r


def RPR_APITest():
    a = _ft['APITest']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_ApplyNudge(p0, p1, p2, p3, p4, p5, p6):
    a = _ft['ApplyNudge']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_int, c_int, c_double, c_byte, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), c_int(p1), c_int(p2), c_int(p3), c_double(p4), c_byte(p5), c_int(p6))
    r = f(t[0], t[1], t[2], t[3], t[4], t[5], t[6])
    return r


def RPR_Audio_IsPreBuffer():
    a = _ft['Audio_IsPreBuffer']
    f = CFUNCTYPE(c_int)(a)
    r = f()
    return r


def RPR_Audio_IsRunning():
    a = _ft['Audio_IsRunning']
    f = CFUNCTYPE(c_int)(a)
    r = f()
    return r


def RPR_Audio_RegHardwareHook(p0, p1):
    a = _ft['Audio_RegHardwareHook']
    f = CFUNCTYPE(c_int, c_byte, c_uint)(a)
    t = (c_byte(p0), rpr_packp('audio_hook_register_t*', p1))
    r = f(t[0], t[1])
    return r


def RPR_BypassFxAllTracks(p0):
    a = _ft['BypassFxAllTracks']
    f = CFUNCTYPE(None, c_int)(a)
    t = (c_int(p0),)
    f(t[0])


def RPR_CalculatePeaks(p0, p1):
    a = _ft['CalculatePeaks']
    f = CFUNCTYPE(c_int, c_uint, c_uint)(a)
    t = (rpr_packp('PCM_source_transfer_t*', p0), rpr_packp('PCM_source_peaktransfer_t*', p1))
    r = f(t[0], t[1])
    return r


def RPR_CalculatePeaksFloatSrcPtr(p0, p1):
    a = _ft['CalculatePeaksFloatSrcPtr']
    f = CFUNCTYPE(c_int, c_uint, c_uint)(a)
    t = (rpr_packp('PCM_source_transfer_t*', p0), rpr_packp('PCM_source_peaktransfer_t*', p1))
    r = f(t[0], t[1])
    return r


def RPR_ClearAllRecArmed():
    a = _ft['ClearAllRecArmed']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_ClearPeakCache():
    a = _ft['ClearPeakCache']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_CountMediaItems(p0):
    a = _ft['CountMediaItems']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    r = f(t[0])
    return r


def RPR_CountSelectedMediaItems(p0):
    a = _ft['CountSelectedMediaItems']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    r = f(t[0])
    return r


def RPR_CountSelectedTracks(p0):
    a = _ft['CountSelectedTracks']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    r = f(t[0])
    return r


def RPR_CountTakes(p0):
    a = _ft['CountTakes']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('MediaItem*', p0),)
    r = f(t[0])
    return r


def RPR_CountTCPFXParms(p0, p1):
    a = _ft['CountTCPFXParms']
    f = CFUNCTYPE(c_int, c_uint, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packp('MediaTrack*', p1))
    r = f(t[0], t[1])
    return r


def RPR_CountTrackEnvelopes(p0):
    a = _ft['CountTrackEnvelopes']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return r


def RPR_CountTrackMediaItems(p0):
    a = _ft['CountTrackMediaItems']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return r


def RPR_CountTracks(p0):
    a = _ft['CountTracks']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    r = f(t[0])
    return r


def RPR_CreateMIDIInput(p0):
    a = _ft['CreateMIDIInput']
    f = CFUNCTYPE(c_uint, c_int)(a)
    t = (c_int(p0),)
    r = f(t[0])
    return rpr_unpackp('midi_Input*', r)


def RPR_CreateMIDIOutput(p0, p1, p2):
    a = _ft['CreateMIDIOutput']
    f = CFUNCTYPE(c_uint, c_int, c_byte, c_void_p)(a)
    t = (c_int(p0), c_byte(p1), c_int(p2))
    r = f(t[0], t[1], byref(t[2]))
    return (rpr_unpackp('midi_Output*', r), p0, p1, int(t[2].value))


def RPR_CreateTakeAudioAccessor(p0):
    a = _ft['CreateTakeAudioAccessor']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('MediaItem_Take*', p0),)
    r = f(t[0])
    return rpr_unpackp('void*', r)


def RPR_CreateTrackAudioAccessor(p0):
    a = _ft['CreateTrackAudioAccessor']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return rpr_unpackp('void*', r)


def RPR_CSurf_FlushUndo(p0):
    a = _ft['CSurf_FlushUndo']
    f = CFUNCTYPE(None, c_byte)(a)
    t = (c_byte(p0),)
    f(t[0])


def RPR_CSurf_GetTouchState(p0, p1):
    a = _ft['CSurf_GetTouchState']
    f = CFUNCTYPE(c_byte, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_CSurf_GoEnd():
    a = _ft['CSurf_GoEnd']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_CSurf_GoStart():
    a = _ft['CSurf_GoStart']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_CSurf_NumTracks(p0):
    a = _ft['CSurf_NumTracks']
    f = CFUNCTYPE(c_int, c_byte)(a)
    t = (c_byte(p0),)
    r = f(t[0])
    return r


def RPR_CSurf_OnArrow(p0, p1):
    a = _ft['CSurf_OnArrow']
    f = CFUNCTYPE(None, c_int, c_byte)(a)
    t = (c_int(p0), c_byte(p1))
    f(t[0], t[1])


def RPR_CSurf_OnFwd(p0):
    a = _ft['CSurf_OnFwd']
    f = CFUNCTYPE(None, c_int)(a)
    t = (c_int(p0),)
    f(t[0])


def RPR_CSurf_OnFXChange(p0, p1):
    a = _ft['CSurf_OnFXChange']
    f = CFUNCTYPE(c_byte, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_CSurf_OnInputMonitorChange(p0, p1):
    a = _ft['CSurf_OnInputMonitorChange']
    f = CFUNCTYPE(c_int, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_CSurf_OnInputMonitorChangeEx(p0, p1, p2):
    a = _ft['CSurf_OnInputMonitorChangeEx']
    f = CFUNCTYPE(c_int, c_uint, c_int, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_byte(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_CSurf_OnMuteChange(p0, p1):
    a = _ft['CSurf_OnMuteChange']
    f = CFUNCTYPE(c_byte, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_CSurf_OnMuteChangeEx(p0, p1, p2):
    a = _ft['CSurf_OnMuteChangeEx']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_byte(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_CSurf_OnPanChange(p0, p1, p2):
    a = _ft['CSurf_OnPanChange']
    f = CFUNCTYPE(c_double, c_uint, c_double, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_double(p1), c_byte(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_CSurf_OnPanChangeEx(p0, p1, p2, p3):
    a = _ft['CSurf_OnPanChangeEx']
    f = CFUNCTYPE(c_double, c_uint, c_double, c_byte, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_double(p1), c_byte(p2), c_byte(p3))
    r = f(t[0], t[1], t[2], t[3])
    return r


def RPR_CSurf_OnPause():
    a = _ft['CSurf_OnPause']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_CSurf_OnPlay():
    a = _ft['CSurf_OnPlay']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_CSurf_OnPlayRateChange(p0):
    a = _ft['CSurf_OnPlayRateChange']
    f = CFUNCTYPE(None, c_double)(a)
    t = (c_double(p0),)
    f(t[0])


def RPR_CSurf_OnRecArmChange(p0, p1):
    a = _ft['CSurf_OnRecArmChange']
    f = CFUNCTYPE(c_byte, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_CSurf_OnRecArmChangeEx(p0, p1, p2):
    a = _ft['CSurf_OnRecArmChangeEx']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_byte(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_CSurf_OnRecord():
    a = _ft['CSurf_OnRecord']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_CSurf_OnRecvPanChange(p0, p1, p2, p3):
    a = _ft['CSurf_OnRecvPanChange']
    f = CFUNCTYPE(c_double, c_uint, c_int, c_double, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_double(p2), c_byte(p3))
    r = f(t[0], t[1], t[2], t[3])
    return r


def RPR_CSurf_OnRecvVolumeChange(p0, p1, p2, p3):
    a = _ft['CSurf_OnRecvVolumeChange']
    f = CFUNCTYPE(c_double, c_uint, c_int, c_double, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_double(p2), c_byte(p3))
    r = f(t[0], t[1], t[2], t[3])
    return r


def RPR_CSurf_OnRew(p0):
    a = _ft['CSurf_OnRew']
    f = CFUNCTYPE(None, c_int)(a)
    t = (c_int(p0),)
    f(t[0])


def RPR_CSurf_OnScroll(p0, p1):
    a = _ft['CSurf_OnScroll']
    f = CFUNCTYPE(None, c_int, c_int)(a)
    t = (c_int(p0), c_int(p1))
    f(t[0], t[1])


def RPR_CSurf_OnSelectedChange(p0, p1):
    a = _ft['CSurf_OnSelectedChange']
    f = CFUNCTYPE(c_byte, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_CSurf_OnSendPanChange(p0, p1, p2, p3):
    a = _ft['CSurf_OnSendPanChange']
    f = CFUNCTYPE(c_double, c_uint, c_int, c_double, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_double(p2), c_byte(p3))
    r = f(t[0], t[1], t[2], t[3])
    return r


def RPR_CSurf_OnSendVolumeChange(p0, p1, p2, p3):
    a = _ft['CSurf_OnSendVolumeChange']
    f = CFUNCTYPE(c_double, c_uint, c_int, c_double, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_double(p2), c_byte(p3))
    r = f(t[0], t[1], t[2], t[3])
    return r


def RPR_CSurf_OnSoloChange(p0, p1):
    a = _ft['CSurf_OnSoloChange']
    f = CFUNCTYPE(c_byte, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_CSurf_OnSoloChangeEx(p0, p1, p2):
    a = _ft['CSurf_OnSoloChangeEx']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_byte(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_CSurf_OnStop():
    a = _ft['CSurf_OnStop']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_CSurf_OnTempoChange(p0):
    a = _ft['CSurf_OnTempoChange']
    f = CFUNCTYPE(None, c_double)(a)
    t = (c_double(p0),)
    f(t[0])


def RPR_CSurf_OnTrackSelection(p0):
    a = _ft['CSurf_OnTrackSelection']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    f(t[0])


def RPR_CSurf_OnVolumeChange(p0, p1, p2):
    a = _ft['CSurf_OnVolumeChange']
    f = CFUNCTYPE(c_double, c_uint, c_double, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_double(p1), c_byte(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_CSurf_OnVolumeChangeEx(p0, p1, p2, p3):
    a = _ft['CSurf_OnVolumeChangeEx']
    f = CFUNCTYPE(c_double, c_uint, c_double, c_byte, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_double(p1), c_byte(p2), c_byte(p3))
    r = f(t[0], t[1], t[2], t[3])
    return r


def RPR_CSurf_OnWidthChange(p0, p1, p2):
    a = _ft['CSurf_OnWidthChange']
    f = CFUNCTYPE(c_double, c_uint, c_double, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_double(p1), c_byte(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_CSurf_OnWidthChangeEx(p0, p1, p2, p3):
    a = _ft['CSurf_OnWidthChangeEx']
    f = CFUNCTYPE(c_double, c_uint, c_double, c_byte, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_double(p1), c_byte(p2), c_byte(p3))
    r = f(t[0], t[1], t[2], t[3])
    return r


def RPR_CSurf_OnZoom(p0, p1):
    a = _ft['CSurf_OnZoom']
    f = CFUNCTYPE(None, c_int, c_int)(a)
    t = (c_int(p0), c_int(p1))
    f(t[0], t[1])


def RPR_CSurf_ResetAllCachedVolPanStates():
    a = _ft['CSurf_ResetAllCachedVolPanStates']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_CSurf_ScrubAmt(p0):
    a = _ft['CSurf_ScrubAmt']
    f = CFUNCTYPE(None, c_double)(a)
    t = (c_double(p0),)
    f(t[0])


def RPR_CSurf_SetAutoMode(p0, p1):
    a = _ft['CSurf_SetAutoMode']
    f = CFUNCTYPE(None, c_int, c_uint)(a)
    t = (c_int(p0), rpr_packp('IReaperControlSurface*', p1))
    f(t[0], t[1])


def RPR_CSurf_SetPlayState(p0, p1, p2, p3):
    a = _ft['CSurf_SetPlayState']
    f = CFUNCTYPE(None, c_byte, c_byte, c_byte, c_uint)(a)
    t = (c_byte(p0), c_byte(p1), c_byte(p2), rpr_packp('IReaperControlSurface*', p3))
    f(t[0], t[1], t[2], t[3])


def RPR_CSurf_SetRepeatState(p0, p1):
    a = _ft['CSurf_SetRepeatState']
    f = CFUNCTYPE(None, c_byte, c_uint)(a)
    t = (c_byte(p0), rpr_packp('IReaperControlSurface*', p1))
    f(t[0], t[1])


def RPR_CSurf_SetSurfaceMute(p0, p1, p2):
    a = _ft['CSurf_SetSurfaceMute']
    f = CFUNCTYPE(None, c_uint, c_byte, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0), c_byte(p1), rpr_packp('IReaperControlSurface*', p2))
    f(t[0], t[1], t[2])


def RPR_CSurf_SetSurfacePan(p0, p1, p2):
    a = _ft['CSurf_SetSurfacePan']
    f = CFUNCTYPE(None, c_uint, c_double, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0), c_double(p1), rpr_packp('IReaperControlSurface*', p2))
    f(t[0], t[1], t[2])


def RPR_CSurf_SetSurfaceRecArm(p0, p1, p2):
    a = _ft['CSurf_SetSurfaceRecArm']
    f = CFUNCTYPE(None, c_uint, c_byte, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0), c_byte(p1), rpr_packp('IReaperControlSurface*', p2))
    f(t[0], t[1], t[2])


def RPR_CSurf_SetSurfaceSelected(p0, p1, p2):
    a = _ft['CSurf_SetSurfaceSelected']
    f = CFUNCTYPE(None, c_uint, c_byte, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0), c_byte(p1), rpr_packp('IReaperControlSurface*', p2))
    f(t[0], t[1], t[2])


def RPR_CSurf_SetSurfaceSolo(p0, p1, p2):
    a = _ft['CSurf_SetSurfaceSolo']
    f = CFUNCTYPE(None, c_uint, c_byte, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0), c_byte(p1), rpr_packp('IReaperControlSurface*', p2))
    f(t[0], t[1], t[2])


def RPR_CSurf_SetSurfaceVolume(p0, p1, p2):
    a = _ft['CSurf_SetSurfaceVolume']
    f = CFUNCTYPE(None, c_uint, c_double, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0), c_double(p1), rpr_packp('IReaperControlSurface*', p2))
    f(t[0], t[1], t[2])


def RPR_CSurf_SetTrackListChange():
    a = _ft['CSurf_SetTrackListChange']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_CSurf_TrackFromID(p0, p1):
    a = _ft['CSurf_TrackFromID']
    f = CFUNCTYPE(c_uint, c_int, c_byte)(a)
    t = (c_int(p0), c_byte(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('MediaTrack*', r)


def RPR_CSurf_TrackToID(p0, p1):
    a = _ft['CSurf_TrackToID']
    f = CFUNCTYPE(c_int, c_uint, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_byte(p1))
    r = f(t[0], t[1])
    return r


def RPR_DB2SLIDER(p0):
    a = _ft['DB2SLIDER']
    f = CFUNCTYPE(c_double, c_double)(a)
    t = (c_double(p0),)
    r = f(t[0])
    return r


def RPR_DeleteExtState(p0, p1, p2):
    a = _ft['DeleteExtState']
    f = CFUNCTYPE(None, c_char_p, c_char_p, c_byte)(a)
    t = (rpr_packsc(p0), rpr_packsc(p1), c_byte(p2))
    f(t[0], t[1], t[2])


def RPR_DeleteProjectMarker(p0, p1, p2):
    a = _ft['DeleteProjectMarker']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_byte)(a)
    t = (rpr_packp('ReaProject*', p0), c_int(p1), c_byte(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_DeleteTrack(p0):
    a = _ft['DeleteTrack']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    f(t[0])


def RPR_DeleteTrackMediaItem(p0, p1):
    a = _ft['DeleteTrackMediaItem']
    f = CFUNCTYPE(c_byte, c_uint, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0), rpr_packp('MediaItem*', p1))
    r = f(t[0], t[1])
    return r


def RPR_DestroyAudioAccessor(p0):
    a = _ft['DestroyAudioAccessor']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('void*', p0),)
    f(t[0])


def RPR_Dock_UpdateDockID(p0, p1):
    a = _ft['Dock_UpdateDockID']
    f = CFUNCTYPE(None, c_char_p, c_int)(a)
    t = (rpr_packs(p0), c_int(p1))
    f(t[0], t[1])
    return (rpr_unpacks(t[0]), p1)


def RPR_DockIsChildOfDock(p0, p1):
    a = _ft['DockIsChildOfDock']
    f = CFUNCTYPE(c_int, c_uint, c_void_p)(a)
    t = (rpr_packp('HWND', p0), c_byte(p1))
    r = f(t[0], byref(t[1]))
    return (r, p0, int(t[1].value))


def RPR_DockWindowActivate(p0):
    a = _ft['DockWindowActivate']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('HWND', p0),)
    f(t[0])


def RPR_DockWindowAdd(p0, p1, p2, p3):
    a = _ft['DockWindowAdd']
    f = CFUNCTYPE(None, c_uint, c_char_p, c_int, c_byte)(a)
    t = (rpr_packp('HWND', p0), rpr_packs(p1), c_int(p2), c_byte(p3))
    f(t[0], t[1], t[2], t[3])
    return (p0, rpr_unpacks(t[1]), p2, p3)


def RPR_DockWindowAddEx(p0, p1, p2, p3):
    a = _ft['DockWindowAddEx']
    f = CFUNCTYPE(None, c_uint, c_char_p, c_char_p, c_byte)(a)
    t = (rpr_packp('HWND', p0), rpr_packs(p1), rpr_packs(p2), c_byte(p3))
    f(t[0], t[1], t[2], t[3])
    return (p0, rpr_unpacks(t[1]), rpr_unpacks(t[2]), p3)


def RPR_DockWindowRefresh():
    a = _ft['DockWindowRefresh']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_DockWindowRemove(p0):
    a = _ft['DockWindowRemove']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('HWND', p0),)
    f(t[0])


def RPR_EnsureNotCompletelyOffscreen(p0):
    a = _ft['EnsureNotCompletelyOffscreen']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('RECT*', p0),)
    f(t[0])


def RPR_EnumPitchShiftModes(p0, p1):
    a = _ft['EnumPitchShiftModes']
    f = CFUNCTYPE(c_byte, c_int, c_uint)(a)
    t = (c_int(p0), rpr_packp('const char**', p1))
    r = f(t[0], t[1])
    return r


def RPR_EnumPitchShiftSubModes(p0, p1):
    a = _ft['EnumPitchShiftSubModes']
    f = CFUNCTYPE(c_char_p, c_int, c_int)(a)
    t = (c_int(p0), c_int(p1))
    r = f(t[0], t[1])
    return str(r.decode())


def RPR_EnumProjectMarkers(p0, p1, p2, p3, p4, p5):
    a = _ft['EnumProjectMarkers']
    f = CFUNCTYPE(c_int, c_int, c_void_p, c_void_p, c_void_p, c_uint, c_void_p)(a)
    t = (c_int(p0), c_byte(p1), c_double(p2), c_double(p3), rpr_packp('char**', p4), c_int(p5))
    r = f(t[0], byref(t[1]), byref(t[2]), byref(t[3]), t[4], byref(t[5]))
    return (r, p0, int(t[1].value), float(t[2].value), float(t[3].value), p4, int(t[5].value))


def RPR_EnumProjectMarkers2(p0, p1, p2, p3, p4, p5, p6):
    a = _ft['EnumProjectMarkers2']
    f = CFUNCTYPE(c_int, c_uint, c_int, c_void_p, c_void_p, c_void_p, c_uint, c_void_p)(a)
    t = (
    rpr_packp('ReaProject*', p0), c_int(p1), c_byte(p2), c_double(p3), c_double(p4), rpr_packp('char**', p5), c_int(p6))
    r = f(t[0], t[1], byref(t[2]), byref(t[3]), byref(t[4]), t[5], byref(t[6]))
    return (r, p0, p1, int(t[2].value), float(t[3].value), float(t[4].value), p5, int(t[6].value))


def RPR_EnumProjectMarkers3(p0, p1, p2, p3, p4, p5, p6, p7):
    a = _ft['EnumProjectMarkers3']
    f = CFUNCTYPE(c_int, c_uint, c_int, c_void_p, c_void_p, c_void_p, c_uint, c_void_p, c_void_p)(a)
    t = (
    rpr_packp('ReaProject*', p0), c_int(p1), c_byte(p2), c_double(p3), c_double(p4), rpr_packp('char**', p5), c_int(p6),
    c_int(p7))
    r = f(t[0], t[1], byref(t[2]), byref(t[3]), byref(t[4]), t[5], byref(t[6]), byref(t[7]))
    return (r, p0, p1, int(t[2].value), float(t[3].value), float(t[4].value), p5, int(t[6].value), int(t[7].value))


def RPR_EnumProjects(p0, p1, p2):
    a = _ft['EnumProjects']
    f = CFUNCTYPE(c_uint, c_int, c_char_p, c_int)(a)
    t = (c_int(p0), rpr_packs(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return (rpr_unpackp('ReaProject*', r), p0, rpr_unpacks(t[1]), p2)


def RPR_EnumTrackMIDIProgramNames(p0, p1, p2, p3):
    a = _ft['EnumTrackMIDIProgramNames']
    f = CFUNCTYPE(c_byte, c_int, c_int, c_char_p, c_int)(a)
    t = (c_int(p0), c_int(p1), rpr_packs(p2), c_int(p3))
    r = f(t[0], t[1], t[2], t[3])
    return (r, p0, p1, rpr_unpacks(t[2]), p3)


def RPR_EnumTrackMIDIProgramNamesEx(p0, p1, p2, p3, p4):
    a = _ft['EnumTrackMIDIProgramNamesEx']
    f = CFUNCTYPE(c_byte, c_uint, c_uint, c_int, c_char_p, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packp('MediaTrack*', p1), c_int(p2), rpr_packs(p3), c_int(p4))
    r = f(t[0], t[1], t[2], t[3], t[4])
    return (r, p0, p1, p2, rpr_unpacks(t[3]), p4)


def RPR_file_exists(p0):
    a = _ft['file_exists']
    f = CFUNCTYPE(c_byte, c_char_p)(a)
    t = (rpr_packsc(p0),)
    r = f(t[0])
    return r


def RPR_format_timestr(p0, p1, p2):
    a = _ft['format_timestr']
    f = CFUNCTYPE(None, c_double, c_char_p, c_int)(a)
    t = (c_double(p0), rpr_packs(p1), c_int(p2))
    f(t[0], t[1], t[2])
    return (p0, rpr_unpacks(t[1]), p2)


def RPR_format_timestr_len(p0, p1, p2, p3, p4):
    a = _ft['format_timestr_len']
    f = CFUNCTYPE(None, c_double, c_char_p, c_int, c_double, c_int)(a)
    t = (c_double(p0), rpr_packs(p1), c_int(p2), c_double(p3), c_int(p4))
    f(t[0], t[1], t[2], t[3], t[4])
    return (p0, rpr_unpacks(t[1]), p2, p3, p4)


def RPR_format_timestr_pos(p0, p1, p2, p3):
    a = _ft['format_timestr_pos']
    f = CFUNCTYPE(None, c_double, c_char_p, c_int, c_int)(a)
    t = (c_double(p0), rpr_packs(p1), c_int(p2), c_int(p3))
    f(t[0], t[1], t[2], t[3])
    return (p0, rpr_unpacks(t[1]), p2, p3)


def RPR_get_config_var(p0, p1):
    a = _ft['get_config_var']
    f = CFUNCTYPE(c_uint, c_char_p, c_void_p)(a)
    t = (rpr_packsc(p0), c_int(p1))
    r = f(t[0], byref(t[1]))
    return (rpr_unpackp('void*', r), p0, int(t[1].value))


def RPR_get_ini_file():
    a = _ft['get_ini_file']
    f = CFUNCTYPE(c_char_p)(a)
    r = f()
    return str(r.decode())


def RPR_get_midi_config_var(p0, p1):
    a = _ft['get_midi_config_var']
    f = CFUNCTYPE(c_uint, c_char_p, c_void_p)(a)
    t = (rpr_packsc(p0), c_int(p1))
    r = f(t[0], byref(t[1]))
    return (rpr_unpackp('void*', r), p0, int(t[1].value))


def RPR_GetActiveTake(p0):
    a = _ft['GetActiveTake']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('MediaItem*', p0),)
    r = f(t[0])
    return rpr_unpackp('MediaItem_Take*', r)


def RPR_GetAppVersion():
    a = _ft['GetAppVersion']
    f = CFUNCTYPE(c_char_p)(a)
    r = f()
    return str(r.decode())


def RPR_GetAudioAccessorEndTime(p0):
    a = _ft['GetAudioAccessorEndTime']
    f = CFUNCTYPE(c_double, c_uint)(a)
    t = (rpr_packp('void*', p0),)
    r = f(t[0])
    return r


def RPR_GetAudioAccessorHash(p0, p1):
    a = _ft['GetAudioAccessorHash']
    f = CFUNCTYPE(None, c_uint, c_char_p)(a)
    t = (rpr_packp('void*', p0), rpr_packs(p1))
    f(t[0], t[1])
    return (p0, rpr_unpacks(t[1]))


def RPR_GetAudioAccessorStartTime(p0):
    a = _ft['GetAudioAccessorStartTime']
    f = CFUNCTYPE(c_double, c_uint)(a)
    t = (rpr_packp('void*', p0),)
    r = f(t[0])
    return r


def RPR_GetColorThemeStruct(p0):
    a = _ft['GetColorThemeStruct']
    f = CFUNCTYPE(c_uint, c_void_p)(a)
    t = (c_int(p0),)
    r = f(byref(t[0]))
    return (rpr_unpackp('void*', r), int(t[0].value))


def RPR_GetConfigWantsDock(p0):
    a = _ft['GetConfigWantsDock']
    f = CFUNCTYPE(c_int, c_char_p)(a)
    t = (rpr_packs(p0),)
    r = f(t[0])
    return (r, rpr_unpacks(t[0]))


def RPR_GetCurrentProjectInLoadSave():
    a = _ft['GetCurrentProjectInLoadSave']
    f = CFUNCTYPE(c_uint)(a)
    r = f()
    return rpr_unpackp('void*', r)


def RPR_GetCursorContext():
    a = _ft['GetCursorContext']
    f = CFUNCTYPE(c_int)(a)
    r = f()
    return r


def RPR_GetCursorPosition():
    a = _ft['GetCursorPosition']
    f = CFUNCTYPE(c_double)(a)
    r = f()
    return r


def RPR_GetCursorPositionEx(p0):
    a = _ft['GetCursorPositionEx']
    f = CFUNCTYPE(c_double, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    r = f(t[0])
    return r


def RPR_GetDisplayedMediaItemColor(p0):
    a = _ft['GetDisplayedMediaItemColor']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('MediaItem*', p0),)
    r = f(t[0])
    return r


def RPR_GetDisplayedMediaItemColor2(p0, p1):
    a = _ft['GetDisplayedMediaItemColor2']
    f = CFUNCTYPE(c_int, c_uint, c_uint)(a)
    t = (rpr_packp('MediaItem*', p0), rpr_packp('MediaItem_Take*', p1))
    r = f(t[0], t[1])
    return r


def RPR_GetEnvelopeName(p0, p1, p2):
    a = _ft['GetEnvelopeName']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p, c_int)(a)
    t = (rpr_packp('TrackEnvelope*', p0), rpr_packs(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return (r, p0, rpr_unpacks(t[1]), p2)


def RPR_GetExePath():
    a = _ft['GetExePath']
    f = CFUNCTYPE(c_char_p)(a)
    r = f()
    return str(r.decode())


def RPR_GetExtState(p0, p1):
    a = _ft['GetExtState']
    f = CFUNCTYPE(c_char_p, c_char_p, c_char_p)(a)
    t = (rpr_packsc(p0), rpr_packsc(p1))
    r = f(t[0], t[1])
    return str(r.decode())


def RPR_GetFocusedFX(p0, p1, p2):
    a = _ft['GetFocusedFX']
    f = CFUNCTYPE(c_byte, c_void_p, c_void_p, c_void_p)(a)
    t = (c_int(p0), c_int(p1), c_int(p2))
    r = f(byref(t[0]), byref(t[1]), byref(t[2]))
    return (r, int(t[0].value), int(t[1].value), int(t[2].value))


def RPR_GetHZoomLevel():
    a = _ft['GetHZoomLevel']
    f = CFUNCTYPE(c_double)(a)
    r = f()
    return r


def RPR_GetIconThemePointer(p0):
    a = _ft['GetIconThemePointer']
    f = CFUNCTYPE(c_uint, c_char_p)(a)
    t = (rpr_packsc(p0),)
    r = f(t[0])
    return rpr_unpackp('void*', r)


def RPR_GetIconThemeStruct(p0):
    a = _ft['GetIconThemeStruct']
    f = CFUNCTYPE(c_uint, c_void_p)(a)
    t = (c_int(p0),)
    r = f(byref(t[0]))
    return (rpr_unpackp('void*', r), int(t[0].value))


def RPR_GetInputChannelName(p0):
    a = _ft['GetInputChannelName']
    f = CFUNCTYPE(c_char_p, c_int)(a)
    t = (c_int(p0),)
    r = f(t[0])
    return str(r.decode())


def RPR_GetItemEditingTime2(p0, p1):
    a = _ft['GetItemEditingTime2']
    f = CFUNCTYPE(c_double, c_uint, c_void_p)(a)
    t = (rpr_packp('PCM_source**', p0), c_int(p1))
    r = f(t[0], byref(t[1]))
    return (r, p0, int(t[1].value))


def RPR_GetItemProjectContext(p0):
    a = _ft['GetItemProjectContext']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('MediaItem*', p0),)
    r = f(t[0])
    return rpr_unpackp('void*', r)


def RPR_GetLastTouchedFX(p0, p1, p2):
    a = _ft['GetLastTouchedFX']
    f = CFUNCTYPE(c_byte, c_void_p, c_void_p, c_void_p)(a)
    t = (c_int(p0), c_int(p1), c_int(p2))
    r = f(byref(t[0]), byref(t[1]), byref(t[2]))
    return (r, int(t[0].value), int(t[1].value), int(t[2].value))


def RPR_GetLastTouchedTrack():
    a = _ft['GetLastTouchedTrack']
    f = CFUNCTYPE(c_uint)(a)
    r = f()
    return rpr_unpackp('MediaTrack*', r)


def RPR_GetMainHwnd():
    a = _ft['GetMainHwnd']
    f = CFUNCTYPE(c_uint)(a)
    r = f()
    return rpr_unpackp('HWND', r)


def RPR_GetMasterMuteSoloFlags():
    a = _ft['GetMasterMuteSoloFlags']
    f = CFUNCTYPE(c_int)(a)
    r = f()
    return r


def RPR_GetMasterTrack(p0):
    a = _ft['GetMasterTrack']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    r = f(t[0])
    return rpr_unpackp('MediaTrack*', r)


def RPR_GetMasterTrackVisibility():
    a = _ft['GetMasterTrackVisibility']
    f = CFUNCTYPE(c_int)(a)
    r = f()
    return r


def RPR_GetMaxMidiInputs():
    a = _ft['GetMaxMidiInputs']
    f = CFUNCTYPE(c_int)(a)
    r = f()
    return r


def RPR_GetMaxMidiOutputs():
    a = _ft['GetMaxMidiOutputs']
    f = CFUNCTYPE(c_int)(a)
    r = f()
    return r


def RPR_GetMediaItem(p0, p1):
    a = _ft['GetMediaItem']
    f = CFUNCTYPE(c_uint, c_uint, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), c_int(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('MediaItem*', r)


def RPR_GetMediaItem_Track(p0):
    a = _ft['GetMediaItem_Track']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('MediaItem*', p0),)
    r = f(t[0])
    return rpr_unpackp('MediaTrack*', r)


def RPR_GetMediaItemInfo_Value(p0, p1):
    a = _ft['GetMediaItemInfo_Value']
    f = CFUNCTYPE(c_double, c_uint, c_char_p)(a)
    t = (rpr_packp('MediaItem*', p0), rpr_packsc(p1))
    r = f(t[0], t[1])
    return r


def RPR_GetMediaItemNumTakes(p0):
    a = _ft['GetMediaItemNumTakes']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('MediaItem*', p0),)
    r = f(t[0])
    return r


def RPR_GetMediaItemTake(p0, p1):
    a = _ft['GetMediaItemTake']
    f = CFUNCTYPE(c_uint, c_uint, c_int)(a)
    t = (rpr_packp('MediaItem*', p0), c_int(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('MediaItem_Take*', r)


def RPR_GetMediaItemTake_Item(p0):
    a = _ft['GetMediaItemTake_Item']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('MediaItem_Take*', p0),)
    r = f(t[0])
    return rpr_unpackp('MediaItem*', r)


def RPR_GetMediaItemTake_Source(p0):
    a = _ft['GetMediaItemTake_Source']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('MediaItem_Take*', p0),)
    r = f(t[0])
    return rpr_unpackp('PCM_source*', r)


def RPR_GetMediaItemTake_Track(p0):
    a = _ft['GetMediaItemTake_Track']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('MediaItem_Take*', p0),)
    r = f(t[0])
    return rpr_unpackp('MediaTrack*', r)


def RPR_GetMediaItemTakeByGUID(p0, p1):
    a = _ft['GetMediaItemTakeByGUID']
    f = CFUNCTYPE(c_uint, c_uint, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packp('GUID*', p1))
    r = f(t[0], t[1])
    return rpr_unpackp('MediaItem_Take*', r)


def RPR_GetMediaItemTakeInfo_Value(p0, p1):
    a = _ft['GetMediaItemTakeInfo_Value']
    f = CFUNCTYPE(c_double, c_uint, c_char_p)(a)
    t = (rpr_packp('MediaItem_Take*', p0), rpr_packsc(p1))
    r = f(t[0], t[1])
    return r


def RPR_GetMediaSourceFileName(p0, p1, p2):
    a = _ft['GetMediaSourceFileName']
    f = CFUNCTYPE(None, c_uint, c_char_p, c_int)(a)
    t = (rpr_packp('PCM_source*', p0), rpr_packs(p1), c_int(p2))
    f(t[0], t[1], t[2])
    return (p0, rpr_unpacks(t[1]), p2)


def RPR_GetMediaSourceNumChannels(p0):
    a = _ft['GetMediaSourceNumChannels']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('PCM_source*', p0),)
    r = f(t[0])
    return r


def RPR_GetMediaSourceSampleRate(p0):
    a = _ft['GetMediaSourceSampleRate']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('PCM_source*', p0),)
    r = f(t[0])
    return r


def RPR_GetMediaSourceType(p0, p1, p2):
    a = _ft['GetMediaSourceType']
    f = CFUNCTYPE(None, c_uint, c_char_p, c_int)(a)
    t = (rpr_packp('PCM_source*', p0), rpr_packs(p1), c_int(p2))
    f(t[0], t[1], t[2])
    return (p0, rpr_unpacks(t[1]), p2)


def RPR_GetMediaTrackInfo_Value(p0, p1):
    a = _ft['GetMediaTrackInfo_Value']
    f = CFUNCTYPE(c_double, c_uint, c_char_p)(a)
    t = (rpr_packp('MediaTrack*', p0), rpr_packsc(p1))
    r = f(t[0], t[1])
    return r


def RPR_GetMidiInput(p0):
    a = _ft['GetMidiInput']
    f = CFUNCTYPE(c_uint, c_int)(a)
    t = (c_int(p0),)
    r = f(t[0])
    return rpr_unpackp('midi_Input*', r)


def RPR_GetMIDIInputName(p0, p1, p2):
    a = _ft['GetMIDIInputName']
    f = CFUNCTYPE(c_byte, c_int, c_char_p, c_int)(a)
    t = (c_int(p0), rpr_packs(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return (r, p0, rpr_unpacks(t[1]), p2)


def RPR_GetMidiOutput(p0):
    a = _ft['GetMidiOutput']
    f = CFUNCTYPE(c_uint, c_int)(a)
    t = (c_int(p0),)
    r = f(t[0])
    return rpr_unpackp('midi_Output*', r)


def RPR_GetMIDIOutputName(p0, p1, p2):
    a = _ft['GetMIDIOutputName']
    f = CFUNCTYPE(c_byte, c_int, c_char_p, c_int)(a)
    t = (c_int(p0), rpr_packs(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return (r, p0, rpr_unpacks(t[1]), p2)


def RPR_GetMixerScroll():
    a = _ft['GetMixerScroll']
    f = CFUNCTYPE(c_uint)(a)
    r = f()
    return rpr_unpackp('MediaTrack*', r)


def RPR_GetMouseModifier(p0, p1, p2, p3):
    a = _ft['GetMouseModifier']
    f = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int)(a)
    t = (rpr_packsc(p0), c_int(p1), rpr_packs(p2), c_int(p3))
    f(t[0], t[1], t[2], t[3])
    return (p0, p1, rpr_unpacks(t[2]), p3)


def RPR_GetNumMIDIInputs():
    a = _ft['GetNumMIDIInputs']
    f = CFUNCTYPE(c_int)(a)
    r = f()
    return r


def RPR_GetNumMIDIOutputs():
    a = _ft['GetNumMIDIOutputs']
    f = CFUNCTYPE(c_int)(a)
    r = f()
    return r


def RPR_GetNumTracks():
    a = _ft['GetNumTracks']
    f = CFUNCTYPE(c_int)(a)
    r = f()
    return r


def RPR_GetOutputChannelName(p0):
    a = _ft['GetOutputChannelName']
    f = CFUNCTYPE(c_char_p, c_int)(a)
    t = (c_int(p0),)
    r = f(t[0])
    return str(r.decode())


def RPR_GetOutputLatency():
    a = _ft['GetOutputLatency']
    f = CFUNCTYPE(c_double)(a)
    r = f()
    return r


def RPR_GetPeakFileName(p0, p1, p2):
    a = _ft['GetPeakFileName']
    f = CFUNCTYPE(None, c_char_p, c_char_p, c_int)(a)
    t = (rpr_packsc(p0), rpr_packs(p1), c_int(p2))
    f(t[0], t[1], t[2])
    return (p0, rpr_unpacks(t[1]), p2)


def RPR_GetPeaksBitmap(p0, p1, p2, p3, p4):
    a = _ft['GetPeaksBitmap']
    f = CFUNCTYPE(c_uint, c_uint, c_double, c_int, c_int, c_uint)(a)
    t = (
    rpr_packp('PCM_source_peaktransfer_t*', p0), c_double(p1), c_int(p2), c_int(p3), rpr_packp('LICE_IBitmap*', p4))
    r = f(t[0], t[1], t[2], t[3], t[4])
    return rpr_unpackp('void*', r)


def RPR_GetPlayPosition():
    a = _ft['GetPlayPosition']
    f = CFUNCTYPE(c_double)(a)
    r = f()
    return r


def RPR_GetPlayPosition2():
    a = _ft['GetPlayPosition2']
    f = CFUNCTYPE(c_double)(a)
    r = f()
    return r


def RPR_GetPlayPosition2Ex(p0):
    a = _ft['GetPlayPosition2Ex']
    f = CFUNCTYPE(c_double, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    r = f(t[0])
    return r


def RPR_GetPlayPositionEx(p0):
    a = _ft['GetPlayPositionEx']
    f = CFUNCTYPE(c_double, c_uint)(a)
    t = (rpr_packp('void*', p0),)
    r = f(t[0])
    return r


def RPR_GetPlayState():
    a = _ft['GetPlayState']
    f = CFUNCTYPE(c_int)(a)
    r = f()
    return r


def RPR_GetPlayStateEx(p0):
    a = _ft['GetPlayStateEx']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    r = f(t[0])
    return r


def RPR_GetProjectPath(p0, p1):
    a = _ft['GetProjectPath']
    f = CFUNCTYPE(None, c_char_p, c_int)(a)
    t = (rpr_packs(p0), c_int(p1))
    f(t[0], t[1])
    return (rpr_unpacks(t[0]), p1)


def RPR_GetProjectPathEx(p0, p1, p2):
    a = _ft['GetProjectPathEx']
    f = CFUNCTYPE(None, c_uint, c_char_p, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packs(p1), c_int(p2))
    f(t[0], t[1], t[2])
    return (p0, rpr_unpacks(t[1]), p2)


def RPR_GetProjectTimeSignature(p0, p1):
    a = _ft['GetProjectTimeSignature']
    f = CFUNCTYPE(None, c_void_p, c_void_p)(a)
    t = (c_double(p0), c_double(p1))
    f(byref(t[0]), byref(t[1]))
    return (float(t[0].value), float(t[1].value))


def RPR_GetProjectTimeSignature2(p0, p1, p2):
    a = _ft['GetProjectTimeSignature2']
    f = CFUNCTYPE(None, c_uint, c_void_p, c_void_p)(a)
    t = (rpr_packp('ReaProject*', p0), c_double(p1), c_double(p2))
    f(t[0], byref(t[1]), byref(t[2]))
    return (p0, float(t[1].value), float(t[2].value))


def RPR_GetResourcePath():
    a = _ft['GetResourcePath']
    f = CFUNCTYPE(c_char_p)(a)
    r = f()
    return str(r.decode())


def RPR_GetSelectedMediaItem(p0, p1):
    a = _ft['GetSelectedMediaItem']
    f = CFUNCTYPE(c_uint, c_uint, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), c_int(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('MediaItem*', r)


def RPR_GetSelectedTrack(p0, p1):
    a = _ft['GetSelectedTrack']
    f = CFUNCTYPE(c_uint, c_uint, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), c_int(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('MediaTrack*', r)


def RPR_GetSelectedTrackEnvelope(p0):
    a = _ft['GetSelectedTrackEnvelope']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    r = f(t[0])
    return rpr_unpackp('TrackEnvelope*', r)


def RPR_GetSet_ArrangeView2(p0, p1, p2, p3, p4, p5):
    a = _ft['GetSet_ArrangeView2']
    f = CFUNCTYPE(None, c_uint, c_byte, c_int, c_int, c_void_p, c_void_p)(a)
    t = (rpr_packp('ReaProject*', p0), c_byte(p1), c_int(p2), c_int(p3), c_double(p4), c_double(p5))
    f(t[0], t[1], t[2], t[3], byref(t[4]), byref(t[5]))
    return (p0, p1, p2, p3, float(t[4].value), float(t[5].value))


def RPR_GetSet_LoopTimeRange(p0, p1, p2, p3, p4):
    a = _ft['GetSet_LoopTimeRange']
    f = CFUNCTYPE(None, c_byte, c_byte, c_void_p, c_void_p, c_byte)(a)
    t = (c_byte(p0), c_byte(p1), c_double(p2), c_double(p3), c_byte(p4))
    f(t[0], t[1], byref(t[2]), byref(t[3]), t[4])
    return (p0, p1, float(t[2].value), float(t[3].value), p4)


def RPR_GetSet_LoopTimeRange2(p0, p1, p2, p3, p4, p5):
    a = _ft['GetSet_LoopTimeRange2']
    f = CFUNCTYPE(None, c_uint, c_byte, c_byte, c_void_p, c_void_p, c_byte)(a)
    t = (rpr_packp('ReaProject*', p0), c_byte(p1), c_byte(p2), c_double(p3), c_double(p4), c_byte(p5))
    f(t[0], t[1], t[2], byref(t[3]), byref(t[4]), t[5])
    return (p0, p1, p2, float(t[3].value), float(t[4].value), p5)


def RPR_GetSetEnvelopeState(p0, p1, p2):
    a = _ft['GetSetEnvelopeState']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p, c_int)(a)
    t = (rpr_packp('TrackEnvelope*', p0), rpr_packs(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return (r, p0, rpr_unpacks(t[1]), p2)


def RPR_GetSetEnvelopeState2(p0, p1, p2, p3):
    a = _ft['GetSetEnvelopeState2']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p, c_int, c_byte)(a)
    t = (rpr_packp('TrackEnvelope*', p0), rpr_packs(p1), c_int(p2), c_byte(p3))
    r = f(t[0], t[1], t[2], t[3])
    return (r, p0, rpr_unpacks(t[1]), p2, p3)


def RPR_GetSetItemState(p0, p1, p2):
    a = _ft['GetSetItemState']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p, c_int)(a)
    t = (rpr_packp('MediaItem*', p0), rpr_packs(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return (r, p0, rpr_unpacks(t[1]), p2)


def RPR_GetSetItemState2(p0, p1, p2, p3):
    a = _ft['GetSetItemState2']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p, c_int, c_byte)(a)
    t = (rpr_packp('MediaItem*', p0), rpr_packs(p1), c_int(p2), c_byte(p3))
    r = f(t[0], t[1], t[2], t[3])
    return (r, p0, rpr_unpacks(t[1]), p2, p3)


def RPR_GetSetMediaItemTakeInfo_String(p0, p1, p2, p3):
    a = _ft['GetSetMediaItemTakeInfo_String']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p, c_char_p, c_byte)(a)
    t = (rpr_packp('MediaItem_Take*', p0), rpr_packsc(p1), rpr_packs(p2), c_byte(p3))
    r = f(t[0], t[1], t[2], t[3])
    return (r, p0, p1, rpr_unpacks(t[2]), p3)


def RPR_GetSetMediaTrackInfo_String(p0, p1, p2, p3):
    a = _ft['GetSetMediaTrackInfo_String']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p, c_char_p, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), rpr_packsc(p1), rpr_packs(p2), c_byte(p3))
    r = f(t[0], t[1], t[2], t[3])
    return (r, p0, p1, rpr_unpacks(t[2]), p3)


def RPR_GetSetRepeat(p0):
    a = _ft['GetSetRepeat']
    f = CFUNCTYPE(c_int, c_int)(a)
    t = (c_int(p0),)
    r = f(t[0])
    return r


def RPR_GetSetRepeatEx(p0, p1):
    a = _ft['GetSetRepeatEx']
    f = CFUNCTYPE(c_int, c_uint, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_GetSetTrackState(p0, p1, p2):
    a = _ft['GetSetTrackState']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), rpr_packs(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return (r, p0, rpr_unpacks(t[1]), p2)


def RPR_GetSetTrackState2(p0, p1, p2, p3):
    a = _ft['GetSetTrackState2']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p, c_int, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), rpr_packs(p1), c_int(p2), c_byte(p3))
    r = f(t[0], t[1], t[2], t[3])
    return (r, p0, rpr_unpacks(t[1]), p2, p3)


def RPR_GetSubProjectFromSource(p0):
    a = _ft['GetSubProjectFromSource']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('PCM_source*', p0),)
    r = f(t[0])
    return rpr_unpackp('ReaProject*', r)


def RPR_GetTake(p0, p1):
    a = _ft['GetTake']
    f = CFUNCTYPE(c_uint, c_uint, c_int)(a)
    t = (rpr_packp('MediaItem*', p0), c_int(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('MediaItem_Take*', r)


def RPR_GetTakeEnvelopeByName(p0, p1):
    a = _ft['GetTakeEnvelopeByName']
    f = CFUNCTYPE(c_uint, c_uint, c_char_p)(a)
    t = (rpr_packp('MediaItem_Take*', p0), rpr_packsc(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('TrackEnvelope*', r)


def RPR_GetTakeName(p0):
    a = _ft['GetTakeName']
    f = CFUNCTYPE(c_char_p, c_uint)(a)
    t = (rpr_packp('MediaItem_Take*', p0),)
    r = f(t[0])
    return str(r.decode())


def RPR_GetTCPFXParm(p0, p1, p2, p3, p4):
    a = _ft['GetTCPFXParm']
    f = CFUNCTYPE(c_byte, c_uint, c_uint, c_int, c_void_p, c_void_p)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packp('MediaTrack*', p1), c_int(p2), c_int(p3), c_int(p4))
    r = f(t[0], t[1], t[2], byref(t[3]), byref(t[4]))
    return (r, p0, p1, p2, int(t[3].value), int(t[4].value))


def RPR_GetTempoMatchPlayRate(p0, p1, p2, p3, p4, p5):
    a = _ft['GetTempoMatchPlayRate']
    f = CFUNCTYPE(c_byte, c_uint, c_double, c_double, c_double, c_void_p, c_void_p)(a)
    t = (rpr_packp('PCM_source*', p0), c_double(p1), c_double(p2), c_double(p3), c_double(p4), c_double(p5))
    r = f(t[0], t[1], t[2], t[3], byref(t[4]), byref(t[5]))
    return (r, p0, p1, p2, p3, float(t[4].value), float(t[5].value))


def RPR_GetToggleCommandState(p0):
    a = _ft['GetToggleCommandState']
    f = CFUNCTYPE(c_int, c_int)(a)
    t = (c_int(p0),)
    r = f(t[0])
    return r


def RPR_GetTooltipWindow():
    a = _ft['GetTooltipWindow']
    f = CFUNCTYPE(c_uint)(a)
    r = f()
    return rpr_unpackp('HWND', r)


def RPR_GetTrack(p0, p1):
    a = _ft['GetTrack']
    f = CFUNCTYPE(c_uint, c_uint, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), c_int(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('MediaTrack*', r)


def RPR_GetTrackAutomationMode(p0):
    a = _ft['GetTrackAutomationMode']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return r


def RPR_GetTrackColor(p0):
    a = _ft['GetTrackColor']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return r


def RPR_GetTrackEnvelope(p0, p1):
    a = _ft['GetTrackEnvelope']
    f = CFUNCTYPE(c_uint, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('TrackEnvelope*', r)


def RPR_GetTrackEnvelopeByName(p0, p1):
    a = _ft['GetTrackEnvelopeByName']
    f = CFUNCTYPE(c_uint, c_uint, c_char_p)(a)
    t = (rpr_packp('MediaTrack*', p0), rpr_packsc(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('TrackEnvelope*', r)


def RPR_GetTrackGUID(p0):
    a = _ft['GetTrackGUID']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return rpr_unpackp('GUID*', r)


def RPR_GetTrackMediaItem(p0, p1):
    a = _ft['GetTrackMediaItem']
    f = CFUNCTYPE(c_uint, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('MediaItem*', r)


def RPR_GetTrackMIDINoteName(p0, p1, p2):
    a = _ft['GetTrackMIDINoteName']
    f = CFUNCTYPE(c_char_p, c_int, c_int, c_int)(a)
    t = (c_int(p0), c_int(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return str(r.decode())


def RPR_GetTrackMIDINoteNameEx(p0, p1, p2, p3):
    a = _ft['GetTrackMIDINoteNameEx']
    f = CFUNCTYPE(c_char_p, c_uint, c_uint, c_int, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packp('MediaTrack*', p1), c_int(p2), c_int(p3))
    r = f(t[0], t[1], t[2], t[3])
    return str(r.decode())


def RPR_GetTrackNumMediaItems(p0):
    a = _ft['GetTrackNumMediaItems']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return r


def RPR_GetTrackReceiveName(p0, p1, p2, p3):
    a = _ft['GetTrackReceiveName']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_char_p, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), rpr_packs(p2), c_int(p3))
    r = f(t[0], t[1], t[2], t[3])
    return (r, p0, p1, rpr_unpacks(t[2]), p3)


def RPR_GetTrackReceiveUIVolPan(p0, p1, p2, p3):
    a = _ft['GetTrackReceiveUIVolPan']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_void_p, c_void_p)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_double(p2), c_double(p3))
    r = f(t[0], t[1], byref(t[2]), byref(t[3]))
    return (r, p0, p1, float(t[2].value), float(t[3].value))


def RPR_GetTrackSendName(p0, p1, p2, p3):
    a = _ft['GetTrackSendName']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_char_p, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), rpr_packs(p2), c_int(p3))
    r = f(t[0], t[1], t[2], t[3])
    return (r, p0, p1, rpr_unpacks(t[2]), p3)


def RPR_GetTrackSendUIVolPan(p0, p1, p2, p3):
    a = _ft['GetTrackSendUIVolPan']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_void_p, c_void_p)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_double(p2), c_double(p3))
    r = f(t[0], t[1], byref(t[2]), byref(t[3]))
    return (r, p0, p1, float(t[2].value), float(t[3].value))


def RPR_GetTrackState(p0, p1):
    a = _ft['GetTrackState']
    f = CFUNCTYPE(c_char_p, c_uint, c_void_p)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], byref(t[1]))
    return (str(r.decode()), p0, int(t[1].value))


def RPR_GetTrackUIPan(p0, p1, p2, p3):
    a = _ft['GetTrackUIPan']
    f = CFUNCTYPE(c_byte, c_uint, c_void_p, c_void_p, c_void_p)(a)
    t = (rpr_packp('MediaTrack*', p0), c_double(p1), c_double(p2), c_int(p3))
    r = f(t[0], byref(t[1]), byref(t[2]), byref(t[3]))
    return (r, p0, float(t[1].value), float(t[2].value), int(t[3].value))


def RPR_GetTrackUIVolPan(p0, p1, p2):
    a = _ft['GetTrackUIVolPan']
    f = CFUNCTYPE(c_byte, c_uint, c_void_p, c_void_p)(a)
    t = (rpr_packp('MediaTrack*', p0), c_double(p1), c_double(p2))
    r = f(t[0], byref(t[1]), byref(t[2]))
    return (r, p0, float(t[1].value), float(t[2].value))


def RPR_GetUserFileNameForRead(p0, p1, p2):
    a = _ft['GetUserFileNameForRead']
    f = CFUNCTYPE(c_byte, c_char_p, c_char_p, c_char_p)(a)
    t = (rpr_packs(p0), rpr_packsc(p1), rpr_packsc(p2))
    r = f(t[0], t[1], t[2])
    return (r, rpr_unpacks(t[0]), p1, p2)


def RPR_GetUserInputs(p0, p1, p2, p3, p4):
    a = _ft['GetUserInputs']
    f = CFUNCTYPE(c_byte, c_char_p, c_int, c_char_p, c_char_p, c_int)(a)
    t = (rpr_packsc(p0), c_int(p1), rpr_packsc(p2), rpr_packs(p3), c_int(p4))
    r = f(t[0], t[1], t[2], t[3], t[4])
    return (r, p0, p1, p2, rpr_unpacks(t[3]), p4)


def RPR_GR_SelectColor(p0, p1):
    a = _ft['GR_SelectColor']
    f = CFUNCTYPE(c_int, c_uint, c_void_p)(a)
    t = (rpr_packp('HWND', p0), c_int(p1))
    r = f(t[0], byref(t[1]))
    return (r, p0, int(t[1].value))


def RPR_GSC_mainwnd(p0):
    a = _ft['GSC_mainwnd']
    f = CFUNCTYPE(c_int, c_int)(a)
    t = (c_int(p0),)
    r = f(t[0])
    return r


def RPR_guidToString(p0, p1):
    a = _ft['guidToString']
    f = CFUNCTYPE(None, c_uint, c_char_p)(a)
    t = (rpr_packp('GUID*', p0), rpr_packs(p1))
    f(t[0], t[1])
    return (p0, rpr_unpacks(t[1]))


def RPR_HasExtState(p0, p1):
    a = _ft['HasExtState']
    f = CFUNCTYPE(c_byte, c_char_p, c_char_p)(a)
    t = (rpr_packsc(p0), rpr_packsc(p1))
    r = f(t[0], t[1])
    return r


def RPR_HasTrackMIDIPrograms(p0):
    a = _ft['HasTrackMIDIPrograms']
    f = CFUNCTYPE(c_char_p, c_int)(a)
    t = (c_int(p0),)
    r = f(t[0])
    return str(r.decode())


def RPR_HasTrackMIDIProgramsEx(p0, p1):
    a = _ft['HasTrackMIDIProgramsEx']
    f = CFUNCTYPE(c_char_p, c_uint, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packp('MediaTrack*', p1))
    r = f(t[0], t[1])
    return str(r.decode())


def RPR_Help_Set(p0, p1):
    a = _ft['Help_Set']
    f = CFUNCTYPE(None, c_char_p, c_byte)(a)
    t = (rpr_packsc(p0), c_byte(p1))
    f(t[0], t[1])


def RPR_HiresPeaksFromSource(p0, p1):
    a = _ft['HiresPeaksFromSource']
    f = CFUNCTYPE(None, c_uint, c_uint)(a)
    t = (rpr_packp('PCM_source*', p0), rpr_packp('PCM_source_peaktransfer_t*', p1))
    f(t[0], t[1])


def RPR_InsertMedia(p0, p1):
    a = _ft['InsertMedia']
    f = CFUNCTYPE(c_int, c_char_p, c_int)(a)
    t = (rpr_packs(p0), c_int(p1))
    r = f(t[0], t[1])
    return (r, rpr_unpacks(t[0]), p1)


def RPR_InsertMediaSection(p0, p1, p2, p3, p4):
    a = _ft['InsertMediaSection']
    f = CFUNCTYPE(c_int, c_char_p, c_int, c_double, c_double, c_double)(a)
    t = (rpr_packs(p0), c_int(p1), c_double(p2), c_double(p3), c_double(p4))
    r = f(t[0], t[1], t[2], t[3], t[4])
    return (r, rpr_unpacks(t[0]), p1, p2, p3, p4)


def RPR_InsertTrackAtIndex(p0, p1):
    a = _ft['InsertTrackAtIndex']
    f = CFUNCTYPE(None, c_int, c_byte)(a)
    t = (c_int(p0), c_byte(p1))
    f(t[0], t[1])


def RPR_IsInRealTimeAudio():
    a = _ft['IsInRealTimeAudio']
    f = CFUNCTYPE(c_int)(a)
    r = f()
    return r


def RPR_IsMediaExtension(p0, p1):
    a = _ft['IsMediaExtension']
    f = CFUNCTYPE(c_byte, c_char_p, c_byte)(a)
    t = (rpr_packsc(p0), c_byte(p1))
    r = f(t[0], t[1])
    return r


def RPR_IsTrackSelected(p0):
    a = _ft['IsTrackSelected']
    f = CFUNCTYPE(c_byte, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return r


def RPR_kbd_OnMidiEvent(p0, p1):
    a = _ft['kbd_OnMidiEvent']
    f = CFUNCTYPE(None, c_uint, c_int)(a)
    t = (rpr_packp('MIDI_event_t*', p0), c_int(p1))
    f(t[0], t[1])


def RPR_kbd_OnMidiList(p0, p1):
    a = _ft['kbd_OnMidiList']
    f = CFUNCTYPE(None, c_uint, c_int)(a)
    t = (rpr_packp('MIDI_eventlist*', p0), c_int(p1))
    f(t[0], t[1])


def RPR_LICE_ClipLine(p0, p1, p2, p3, p4, p5, p6, p7):
    a = _ft['LICE_ClipLine']
    f = CFUNCTYPE(c_byte, c_void_p, c_void_p, c_void_p, c_void_p, c_int, c_int, c_int, c_int)(a)
    t = (c_int(p0), c_int(p1), c_int(p2), c_int(p3), c_int(p4), c_int(p5), c_int(p6), c_int(p7))
    r = f(byref(t[0]), byref(t[1]), byref(t[2]), byref(t[3]), t[4], t[5], t[6], t[7])
    return (r, int(t[0].value), int(t[1].value), int(t[2].value), int(t[3].value), p4, p5, p6, p7)


def RPR_Loop_OnArrow(p0, p1):
    a = _ft['Loop_OnArrow']
    f = CFUNCTYPE(c_byte, c_uint, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_Main_OnCommand(p0, p1):
    a = _ft['Main_OnCommand']
    f = CFUNCTYPE(None, c_int, c_int)(a)
    t = (c_int(p0), c_int(p1))
    f(t[0], t[1])


def RPR_Main_OnCommandEx(p0, p1, p2):
    a = _ft['Main_OnCommandEx']
    f = CFUNCTYPE(None, c_int, c_int, c_uint)(a)
    t = (c_int(p0), c_int(p1), rpr_packp('ReaProject*', p2))
    f(t[0], t[1], t[2])


def RPR_Main_openProject(p0):
    a = _ft['Main_openProject']
    f = CFUNCTYPE(None, c_char_p)(a)
    t = (rpr_packs(p0),)
    f(t[0])
    return (rpr_unpacks(t[0]))


def RPR_Main_UpdateLoopInfo(p0):
    a = _ft['Main_UpdateLoopInfo']
    f = CFUNCTYPE(None, c_int)(a)
    t = (c_int(p0),)
    f(t[0])


def RPR_Master_GetPlayRate(p0):
    a = _ft['Master_GetPlayRate']
    f = CFUNCTYPE(c_double, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    r = f(t[0])
    return r


def RPR_Master_GetPlayRateAtTime(p0, p1):
    a = _ft['Master_GetPlayRateAtTime']
    f = CFUNCTYPE(c_double, c_double, c_uint)(a)
    t = (c_double(p0), rpr_packp('ReaProject*', p1))
    r = f(t[0], t[1])
    return r


def RPR_Master_GetTempo():
    a = _ft['Master_GetTempo']
    f = CFUNCTYPE(c_double)(a)
    r = f()
    return r


def RPR_Master_NormalizePlayRate(p0, p1):
    a = _ft['Master_NormalizePlayRate']
    f = CFUNCTYPE(c_double, c_double, c_byte)(a)
    t = (c_double(p0), c_byte(p1))
    r = f(t[0], t[1])
    return r


def RPR_Master_NormalizeTempo(p0, p1):
    a = _ft['Master_NormalizeTempo']
    f = CFUNCTYPE(c_double, c_double, c_byte)(a)
    t = (c_double(p0), c_byte(p1))
    r = f(t[0], t[1])
    return r


def RPR_MB(p0, p1, p2):
    a = _ft['MB']
    f = CFUNCTYPE(c_int, c_char_p, c_char_p, c_int)(a)
    t = (rpr_packsc(p0), rpr_packsc(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_MIDI_eventlist_Create():
    a = _ft['MIDI_eventlist_Create']
    f = CFUNCTYPE(c_uint)(a)
    r = f()
    return rpr_unpackp('MIDI_eventlist*', r)


def RPR_MIDI_eventlist_Destroy(p0):
    a = _ft['MIDI_eventlist_Destroy']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('MIDI_eventlist*', p0),)
    f(t[0])


def RPR_midi_reinit():
    a = _ft['midi_reinit']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_MIDIEditor_GetActive():
    a = _ft['MIDIEditor_GetActive']
    f = CFUNCTYPE(c_uint)(a)
    r = f()
    return rpr_unpackp('void*', r)


def RPR_MIDIEditor_GetMode(p0):
    a = _ft['MIDIEditor_GetMode']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('void*', p0),)
    r = f(t[0])
    return r


def RPR_MIDIEditor_GetTake(p0):
    a = _ft['MIDIEditor_GetTake']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('void*', p0),)
    r = f(t[0])
    return rpr_unpackp('MediaItem_Take*', r)


def RPR_MIDIEditor_LastFocused_OnCommand(p0, p1):
    a = _ft['MIDIEditor_LastFocused_OnCommand']
    f = CFUNCTYPE(c_byte, c_int, c_byte)(a)
    t = (c_int(p0), c_byte(p1))
    r = f(t[0], t[1])
    return r


def RPR_MIDIEditor_OnCommand(p0, p1):
    a = _ft['MIDIEditor_OnCommand']
    f = CFUNCTYPE(c_byte, c_uint, c_int)(a)
    t = (rpr_packp('void*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_mkpanstr(p0, p1):
    a = _ft['mkpanstr']
    f = CFUNCTYPE(None, c_char_p, c_double)(a)
    t = (rpr_packs(p0), c_double(p1))
    f(t[0], t[1])
    return (rpr_unpacks(t[0]), p1)


def RPR_mkvolpanstr(p0, p1, p2):
    a = _ft['mkvolpanstr']
    f = CFUNCTYPE(None, c_char_p, c_double, c_double)(a)
    t = (rpr_packs(p0), c_double(p1), c_double(p2))
    f(t[0], t[1], t[2])
    return (rpr_unpacks(t[0]), p1, p2)


def RPR_mkvolstr(p0, p1):
    a = _ft['mkvolstr']
    f = CFUNCTYPE(None, c_char_p, c_double)(a)
    t = (rpr_packs(p0), c_double(p1))
    f(t[0], t[1])
    return (rpr_unpacks(t[0]), p1)


def RPR_MoveEditCursor(p0, p1):
    a = _ft['MoveEditCursor']
    f = CFUNCTYPE(None, c_double, c_byte)(a)
    t = (c_double(p0), c_byte(p1))
    f(t[0], t[1])


def RPR_MoveMediaItemToTrack(p0, p1):
    a = _ft['MoveMediaItemToTrack']
    f = CFUNCTYPE(c_byte, c_uint, c_uint)(a)
    t = (rpr_packp('MediaItem*', p0), rpr_packp('MediaTrack*', p1))
    r = f(t[0], t[1])
    return r


def RPR_MuteAllTracks(p0):
    a = _ft['MuteAllTracks']
    f = CFUNCTYPE(None, c_byte)(a)
    t = (c_byte(p0),)
    f(t[0])


def RPR_my_getViewport(p0, p1, p2):
    a = _ft['my_getViewport']
    f = CFUNCTYPE(None, c_uint, c_uint, c_byte)(a)
    t = (rpr_packp('RECT*', p0), rpr_packp('RECT*', p1), c_byte(p2))
    f(t[0], t[1], t[2])


def RPR_NamedCommandLookup(p0):
    a = _ft['NamedCommandLookup']
    f = CFUNCTYPE(c_int, c_char_p)(a)
    t = (rpr_packsc(p0),)
    r = f(t[0])
    return r


def RPR_OnPauseButton():
    a = _ft['OnPauseButton']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_OnPauseButtonEx(p0):
    a = _ft['OnPauseButtonEx']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    f(t[0])


def RPR_OnPlayButton():
    a = _ft['OnPlayButton']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_OnPlayButtonEx(p0):
    a = _ft['OnPlayButtonEx']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    f(t[0])


def RPR_OnStopButton():
    a = _ft['OnStopButton']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_OnStopButtonEx(p0):
    a = _ft['OnStopButtonEx']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    f(t[0])


def RPR_OscLocalMessageToHost(p0, p1):
    a = _ft['OscLocalMessageToHost']
    f = CFUNCTYPE(None, c_char_p, c_void_p)(a)
    t = (rpr_packsc(p0), c_double(p1))
    f(t[0], byref(t[1]))
    return (p0, float(t[1].value))


def RPR_parse_timestr(p0):
    a = _ft['parse_timestr']
    f = CFUNCTYPE(c_double, c_char_p)(a)
    t = (rpr_packsc(p0),)
    r = f(t[0])
    return r


def RPR_parse_timestr_len(p0, p1, p2):
    a = _ft['parse_timestr_len']
    f = CFUNCTYPE(c_double, c_char_p, c_double, c_int)(a)
    t = (rpr_packsc(p0), c_double(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_parse_timestr_pos(p0, p1):
    a = _ft['parse_timestr_pos']
    f = CFUNCTYPE(c_double, c_char_p, c_int)(a)
    t = (rpr_packsc(p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_parsepanstr(p0):
    a = _ft['parsepanstr']
    f = CFUNCTYPE(c_double, c_char_p)(a)
    t = (rpr_packs(p0),)
    r = f(t[0])
    return (r, rpr_unpacks(t[0]))


def RPR_PCM_Sink_Create(p0, p1, p2, p3, p4, p5):
    a = _ft['PCM_Sink_Create']
    f = CFUNCTYPE(c_uint, c_char_p, c_char_p, c_int, c_int, c_int, c_byte)(a)
    t = (rpr_packsc(p0), rpr_packsc(p1), c_int(p2), c_int(p3), c_int(p4), c_byte(p5))
    r = f(t[0], t[1], t[2], t[3], t[4], t[5])
    return rpr_unpackp('PCM_sink*', r)


def RPR_PCM_Sink_CreateEx(p0, p1, p2, p3, p4, p5, p6):
    a = _ft['PCM_Sink_CreateEx']
    f = CFUNCTYPE(c_uint, c_uint, c_char_p, c_char_p, c_int, c_int, c_int, c_byte)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packsc(p1), rpr_packsc(p2), c_int(p3), c_int(p4), c_int(p5), c_byte(p6))
    r = f(t[0], t[1], t[2], t[3], t[4], t[5], t[6])
    return rpr_unpackp('PCM_sink*', r)


def RPR_PCM_Sink_CreateMIDIFile(p0, p1, p2, p3, p4):
    a = _ft['PCM_Sink_CreateMIDIFile']
    f = CFUNCTYPE(c_uint, c_char_p, c_char_p, c_int, c_double, c_int)(a)
    t = (rpr_packsc(p0), rpr_packsc(p1), c_int(p2), c_double(p3), c_int(p4))
    r = f(t[0], t[1], t[2], t[3], t[4])
    return rpr_unpackp('PCM_sink*', r)


def RPR_PCM_Sink_CreateMIDIFileEx(p0, p1, p2, p3, p4, p5):
    a = _ft['PCM_Sink_CreateMIDIFileEx']
    f = CFUNCTYPE(c_uint, c_uint, c_char_p, c_char_p, c_int, c_double, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packsc(p1), rpr_packsc(p2), c_int(p3), c_double(p4), c_int(p5))
    r = f(t[0], t[1], t[2], t[3], t[4], t[5])
    return rpr_unpackp('PCM_sink*', r)


def RPR_PCM_Sink_Enum(p0, p1):
    a = _ft['PCM_Sink_Enum']
    f = CFUNCTYPE(c_int, c_int, c_uint)(a)
    t = (c_int(p0), rpr_packp('const char**', p1))
    r = f(t[0], t[1])
    return r


def RPR_PCM_Sink_GetExtension(p0, p1):
    a = _ft['PCM_Sink_GetExtension']
    f = CFUNCTYPE(c_char_p, c_uint, c_int)(a)
    t = (rpr_packp('const void*', p0), c_int(p1))
    r = f(t[0], t[1])
    return str(r.decode())


def RPR_PCM_Sink_ShowConfig(p0, p1, p2):
    a = _ft['PCM_Sink_ShowConfig']
    f = CFUNCTYPE(c_uint, c_uint, c_int, c_uint)(a)
    t = (rpr_packp('const void*', p0), c_int(p1), rpr_packp('HWND', p2))
    r = f(t[0], t[1], t[2])
    return rpr_unpackp('HWND', r)


def RPR_PCM_Source_CreateFromFile(p0):
    a = _ft['PCM_Source_CreateFromFile']
    f = CFUNCTYPE(c_uint, c_char_p)(a)
    t = (rpr_packsc(p0),)
    r = f(t[0])
    return rpr_unpackp('PCM_source*', r)


def RPR_PCM_Source_CreateFromFileEx(p0, p1):
    a = _ft['PCM_Source_CreateFromFileEx']
    f = CFUNCTYPE(c_uint, c_char_p, c_byte)(a)
    t = (rpr_packsc(p0), c_byte(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('PCM_source*', r)


def RPR_PCM_Source_CreateFromSimple(p0, p1):
    a = _ft['PCM_Source_CreateFromSimple']
    f = CFUNCTYPE(c_uint, c_uint, c_char_p)(a)
    t = (rpr_packp('ISimpleMediaDecoder*', p0), rpr_packsc(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('PCM_source*', r)


def RPR_PCM_Source_CreateFromType(p0):
    a = _ft['PCM_Source_CreateFromType']
    f = CFUNCTYPE(c_uint, c_char_p)(a)
    t = (rpr_packsc(p0),)
    r = f(t[0])
    return rpr_unpackp('PCM_source*', r)


def RPR_PeakBuild_Create(p0, p1, p2, p3):
    a = _ft['PeakBuild_Create']
    f = CFUNCTYPE(c_uint, c_uint, c_char_p, c_int, c_int)(a)
    t = (rpr_packp('PCM_source*', p0), rpr_packsc(p1), c_int(p2), c_int(p3))
    r = f(t[0], t[1], t[2], t[3])
    return rpr_unpackp('REAPER_PeakBuild_Interface*', r)


def RPR_PeakGet_Create(p0, p1, p2):
    a = _ft['PeakGet_Create']
    f = CFUNCTYPE(c_uint, c_char_p, c_int, c_int)(a)
    t = (rpr_packsc(p0), c_int(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return rpr_unpackp('REAPER_PeakGet_Interface*', r)


def RPR_PlayPreview(p0):
    a = _ft['PlayPreview']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('preview_register_t*', p0),)
    r = f(t[0])
    return r


def RPR_PlayPreviewEx(p0, p1, p2):
    a = _ft['PlayPreviewEx']
    f = CFUNCTYPE(c_int, c_uint, c_int, c_double)(a)
    t = (rpr_packp('preview_register_t*', p0), c_int(p1), c_double(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_PlayTrackPreview(p0):
    a = _ft['PlayTrackPreview']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('preview_register_t*', p0),)
    r = f(t[0])
    return r


def RPR_PlayTrackPreview2(p0, p1):
    a = _ft['PlayTrackPreview2']
    f = CFUNCTYPE(c_int, c_uint, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packp('preview_register_t*', p1))
    r = f(t[0], t[1])
    return r


def RPR_PlayTrackPreview2Ex(p0, p1, p2, p3):
    a = _ft['PlayTrackPreview2Ex']
    f = CFUNCTYPE(c_int, c_uint, c_uint, c_int, c_double)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packp('preview_register_t*', p1), c_int(p2), c_double(p3))
    r = f(t[0], t[1], t[2], t[3])
    return r


def RPR_plugin_getFilterList():
    a = _ft['plugin_getFilterList']
    f = CFUNCTYPE(c_char_p)(a)
    r = f()
    return r


def RPR_plugin_getImportableProjectFilterList():
    a = _ft['plugin_getImportableProjectFilterList']
    f = CFUNCTYPE(c_char_p)(a)
    r = f()
    return r


def RPR_PluginWantsAlwaysRunFx(p0):
    a = _ft['PluginWantsAlwaysRunFx']
    f = CFUNCTYPE(None, c_int)(a)
    t = (c_int(p0),)
    f(t[0])


def RPR_projectconfig_var_addr(p0, p1):
    a = _ft['projectconfig_var_addr']
    f = CFUNCTYPE(c_uint, c_uint, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), c_int(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('void*', r)


def RPR_projectconfig_var_getoffs(p0, p1):
    a = _ft['projectconfig_var_getoffs']
    f = CFUNCTYPE(c_int, c_char_p, c_void_p)(a)
    t = (rpr_packsc(p0), c_int(p1))
    r = f(t[0], byref(t[1]))
    return (r, p0, int(t[1].value))


def RPR_ReaperGetPitchShiftAPI(p0):
    a = _ft['ReaperGetPitchShiftAPI']
    f = CFUNCTYPE(c_uint, c_int)(a)
    t = (c_int(p0),)
    r = f(t[0])
    return rpr_unpackp('IReaperPitchShift*', r)


def RPR_ReaScriptError(p0):
    a = _ft['ReaScriptError']
    f = CFUNCTYPE(None, c_char_p)(a)
    t = (rpr_packsc(p0),)
    f(t[0])


def RPR_relative_fn(p0, p1, p2):
    a = _ft['relative_fn']
    f = CFUNCTYPE(None, c_char_p, c_char_p, c_int)(a)
    t = (rpr_packsc(p0), rpr_packs(p1), c_int(p2))
    f(t[0], t[1], t[2])
    return (p0, rpr_unpacks(t[1]), p2)


def RPR_RenderFileSection(p0, p1, p2, p3, p4):
    a = _ft['RenderFileSection']
    f = CFUNCTYPE(c_byte, c_char_p, c_char_p, c_double, c_double, c_double)(a)
    t = (rpr_packsc(p0), rpr_packsc(p1), c_double(p2), c_double(p3), c_double(p4))
    r = f(t[0], t[1], t[2], t[3], t[4])
    return r


def RPR_Resample_EnumModes(p0):
    a = _ft['Resample_EnumModes']
    f = CFUNCTYPE(c_char_p, c_int)(a)
    t = (c_int(p0),)
    r = f(t[0])
    return str(r.decode())


def RPR_Resampler_Create():
    a = _ft['Resampler_Create']
    f = CFUNCTYPE(c_uint)(a)
    r = f()
    return rpr_unpackp('REAPER_Resample_Interface*', r)


def RPR_resolve_fn(p0, p1, p2):
    a = _ft['resolve_fn']
    f = CFUNCTYPE(None, c_char_p, c_char_p, c_int)(a)
    t = (rpr_packsc(p0), rpr_packs(p1), c_int(p2))
    f(t[0], t[1], t[2])
    return (p0, rpr_unpacks(t[1]), p2)


def RPR_screenset_unregister(p0):
    a = _ft['screenset_unregister']
    f = CFUNCTYPE(None, c_char_p)(a)
    t = (rpr_packs(p0),)
    f(t[0])
    return (rpr_unpacks(t[0]))


def RPR_screenset_unregisterByParam(p0):
    a = _ft['screenset_unregisterByParam']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('void*', p0),)
    f(t[0])


def RPR_SelectProjectInstance(p0):
    a = _ft['SelectProjectInstance']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0),)
    f(t[0])


def RPR_SetAutomationMode(p0, p1):
    a = _ft['SetAutomationMode']
    f = CFUNCTYPE(None, c_int, c_byte)(a)
    t = (c_int(p0), c_byte(p1))
    f(t[0], t[1])


def RPR_SetCurrentBPM(p0, p1, p2):
    a = _ft['SetCurrentBPM']
    f = CFUNCTYPE(None, c_uint, c_double, c_byte)(a)
    t = (rpr_packp('ReaProject*', p0), c_double(p1), c_byte(p2))
    f(t[0], t[1], t[2])


def RPR_SetEditCurPos(p0, p1, p2):
    a = _ft['SetEditCurPos']
    f = CFUNCTYPE(None, c_double, c_byte, c_byte)(a)
    t = (c_double(p0), c_byte(p1), c_byte(p2))
    f(t[0], t[1], t[2])


def RPR_SetEditCurPos2(p0, p1, p2, p3):
    a = _ft['SetEditCurPos2']
    f = CFUNCTYPE(None, c_uint, c_double, c_byte, c_byte)(a)
    t = (rpr_packp('ReaProject*', p0), c_double(p1), c_byte(p2), c_byte(p3))
    f(t[0], t[1], t[2], t[3])


def RPR_SetExtState(p0, p1, p2, p3):
    a = _ft['SetExtState']
    f = CFUNCTYPE(None, c_char_p, c_char_p, c_char_p, c_byte)(a)
    t = (rpr_packsc(p0), rpr_packsc(p1), rpr_packsc(p2), c_byte(p3))
    f(t[0], t[1], t[2], t[3])


def RPR_SetMasterTrackVisibility(p0):
    a = _ft['SetMasterTrackVisibility']
    f = CFUNCTYPE(c_int, c_int)(a)
    t = (c_int(p0),)
    r = f(t[0])
    return r


def RPR_SetMediaItemInfo_Value(p0, p1, p2):
    a = _ft['SetMediaItemInfo_Value']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p, c_double)(a)
    t = (rpr_packp('MediaItem*', p0), rpr_packsc(p1), c_double(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_SetMediaItemLength(p0, p1, p2):
    a = _ft['SetMediaItemLength']
    f = CFUNCTYPE(c_byte, c_uint, c_double, c_byte)(a)
    t = (rpr_packp('MediaItem*', p0), c_double(p1), c_byte(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_SetMediaItemPosition(p0, p1, p2):
    a = _ft['SetMediaItemPosition']
    f = CFUNCTYPE(c_byte, c_uint, c_double, c_byte)(a)
    t = (rpr_packp('MediaItem*', p0), c_double(p1), c_byte(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_SetMediaItemTakeInfo_Value(p0, p1, p2):
    a = _ft['SetMediaItemTakeInfo_Value']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p, c_double)(a)
    t = (rpr_packp('MediaItem_Take*', p0), rpr_packsc(p1), c_double(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_SetMediaTrackInfo_Value(p0, p1, p2):
    a = _ft['SetMediaTrackInfo_Value']
    f = CFUNCTYPE(c_byte, c_uint, c_char_p, c_double)(a)
    t = (rpr_packp('MediaTrack*', p0), rpr_packsc(p1), c_double(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_SetMixerScroll(p0):
    a = _ft['SetMixerScroll']
    f = CFUNCTYPE(c_uint, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return rpr_unpackp('MediaTrack*', r)


def RPR_SetMouseModifier(p0, p1, p2):
    a = _ft['SetMouseModifier']
    f = CFUNCTYPE(None, c_char_p, c_int, c_char_p)(a)
    t = (rpr_packsc(p0), c_int(p1), rpr_packsc(p2))
    f(t[0], t[1], t[2])


def RPR_SetOnlyTrackSelected(p0):
    a = _ft['SetOnlyTrackSelected']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    f(t[0])


def RPR_SetProjectMarker(p0, p1, p2, p3, p4):
    a = _ft['SetProjectMarker']
    f = CFUNCTYPE(c_byte, c_int, c_byte, c_double, c_double, c_char_p)(a)
    t = (c_int(p0), c_byte(p1), c_double(p2), c_double(p3), rpr_packsc(p4))
    r = f(t[0], t[1], t[2], t[3], t[4])
    return r


def RPR_SetProjectMarker2(p0, p1, p2, p3, p4, p5):
    a = _ft['SetProjectMarker2']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_byte, c_double, c_double, c_char_p)(a)
    t = (rpr_packp('ReaProject*', p0), c_int(p1), c_byte(p2), c_double(p3), c_double(p4), rpr_packsc(p5))
    r = f(t[0], t[1], t[2], t[3], t[4], t[5])
    return r


def RPR_SetProjectMarker3(p0, p1, p2, p3, p4, p5, p6):
    a = _ft['SetProjectMarker3']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_byte, c_double, c_double, c_char_p, c_int)(a)
    t = (rpr_packp('ReaProject*', p0), c_int(p1), c_byte(p2), c_double(p3), c_double(p4), rpr_packsc(p5), c_int(p6))
    r = f(t[0], t[1], t[2], t[3], t[4], t[5], t[6])
    return r


def RPR_SetRenderLastError(p0):
    a = _ft['SetRenderLastError']
    f = CFUNCTYPE(None, c_char_p)(a)
    t = (rpr_packs(p0),)
    f(t[0])
    return (rpr_unpacks(t[0]))


def RPR_SetTrackAutomationMode(p0, p1):
    a = _ft['SetTrackAutomationMode']
    f = CFUNCTYPE(None, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    f(t[0], t[1])


def RPR_SetTrackColor(p0, p1):
    a = _ft['SetTrackColor']
    f = CFUNCTYPE(None, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    f(t[0], t[1])


def RPR_SetTrackMIDINoteName(p0, p1, p2, p3):
    a = _ft['SetTrackMIDINoteName']
    f = CFUNCTYPE(c_char_p, c_int, c_int, c_int, c_char_p)(a)
    t = (c_int(p0), c_int(p1), c_int(p2), rpr_packsc(p3))
    r = f(t[0], t[1], t[2], t[3])
    return str(r.decode())


def RPR_SetTrackMIDINoteNameEx(p0, p1, p2, p3, p4):
    a = _ft['SetTrackMIDINoteNameEx']
    f = CFUNCTYPE(c_char_p, c_uint, c_uint, c_int, c_int, c_char_p)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packp('MediaTrack*', p1), c_int(p2), c_int(p3), rpr_packsc(p4))
    r = f(t[0], t[1], t[2], t[3], t[4])
    return str(r.decode())


def RPR_SetTrackSelected(p0, p1):
    a = _ft['SetTrackSelected']
    f = CFUNCTYPE(None, c_uint, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_byte(p1))
    f(t[0], t[1])


def RPR_ShowActionList(p0, p1):
    a = _ft['ShowActionList']
    f = CFUNCTYPE(None, c_uint, c_uint)(a)
    t = (rpr_packp('KbdSectionInfo*', p0), rpr_packp('HWND', p1))
    f(t[0], t[1])


def RPR_ShowConsoleMsg(p0):
    a = _ft['ShowConsoleMsg']
    f = CFUNCTYPE(None, c_char_p)(a)
    t = (rpr_packsc(p0),)
    f(t[0])


def RPR_ShowMessageBox(p0, p1, p2):
    a = _ft['ShowMessageBox']
    f = CFUNCTYPE(c_int, c_char_p, c_char_p, c_int)(a)
    t = (rpr_packsc(p0), rpr_packsc(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_SLIDER2DB(p0):
    a = _ft['SLIDER2DB']
    f = CFUNCTYPE(c_double, c_double)(a)
    t = (c_double(p0),)
    r = f(t[0])
    return r


def RPR_SnapToGrid(p0, p1):
    a = _ft['SnapToGrid']
    f = CFUNCTYPE(c_double, c_uint, c_double)(a)
    t = (rpr_packp('ReaProject*', p0), c_double(p1))
    r = f(t[0], t[1])
    return r


def RPR_SoloAllTracks(p0):
    a = _ft['SoloAllTracks']
    f = CFUNCTYPE(None, c_int)(a)
    t = (c_int(p0),)
    f(t[0])


def RPR_SplitMediaItem(p0, p1):
    a = _ft['SplitMediaItem']
    f = CFUNCTYPE(c_uint, c_uint, c_double)(a)
    t = (rpr_packp('MediaItem*', p0), c_double(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('MediaItem*', r)


def RPR_StopPreview(p0):
    a = _ft['StopPreview']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('preview_register_t*', p0),)
    r = f(t[0])
    return r


def RPR_StopTrackPreview(p0):
    a = _ft['StopTrackPreview']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('preview_register_t*', p0),)
    r = f(t[0])
    return r


def RPR_StopTrackPreview2(p0, p1):
    a = _ft['StopTrackPreview2']
    f = CFUNCTYPE(c_int, c_uint, c_uint)(a)
    t = (rpr_packp('void*', p0), rpr_packp('preview_register_t*', p1))
    r = f(t[0], t[1])
    return r


def RPR_stringToGuid(p0, p1):
    a = _ft['stringToGuid']
    f = CFUNCTYPE(None, c_char_p, c_uint)(a)
    t = (rpr_packsc(p0), rpr_packp('GUID*', p1))
    f(t[0], t[1])


def RPR_TimeMap2_beatsToTime(p0, p1, p2):
    a = _ft['TimeMap2_beatsToTime']
    f = CFUNCTYPE(c_double, c_uint, c_double, c_void_p)(a)
    t = (rpr_packp('ReaProject*', p0), c_double(p1), c_int(p2))
    r = f(t[0], t[1], byref(t[2]))
    return (r, p0, p1, int(t[2].value))


def RPR_TimeMap2_GetDividedBpmAtTime(p0, p1):
    a = _ft['TimeMap2_GetDividedBpmAtTime']
    f = CFUNCTYPE(c_double, c_uint, c_double)(a)
    t = (rpr_packp('ReaProject*', p0), c_double(p1))
    r = f(t[0], t[1])
    return r


def RPR_TimeMap2_GetNextChangeTime(p0, p1):
    a = _ft['TimeMap2_GetNextChangeTime']
    f = CFUNCTYPE(c_double, c_uint, c_double)(a)
    t = (rpr_packp('ReaProject*', p0), c_double(p1))
    r = f(t[0], t[1])
    return r


def RPR_TimeMap2_QNToTime(p0, p1):
    a = _ft['TimeMap2_QNToTime']
    f = CFUNCTYPE(c_double, c_uint, c_double)(a)
    t = (rpr_packp('ReaProject*', p0), c_double(p1))
    r = f(t[0], t[1])
    return r


def RPR_TimeMap2_timeToBeats(p0, p1, p2, p3, p4, p5):
    a = _ft['TimeMap2_timeToBeats']
    f = CFUNCTYPE(c_double, c_uint, c_double, c_void_p, c_void_p, c_void_p, c_void_p)(a)
    t = (rpr_packp('ReaProject*', p0), c_double(p1), c_int(p2), c_int(p3), c_double(p4), c_int(p5))
    r = f(t[0], t[1], byref(t[2]), byref(t[3]), byref(t[4]), byref(t[5]))
    return (r, p0, p1, int(t[2].value), int(t[3].value), float(t[4].value), int(t[5].value))


def RPR_TimeMap2_timeToQN(p0, p1):
    a = _ft['TimeMap2_timeToQN']
    f = CFUNCTYPE(c_double, c_uint, c_double)(a)
    t = (rpr_packp('ReaProject*', p0), c_double(p1))
    r = f(t[0], t[1])
    return r


def RPR_TimeMap_GetDividedBpmAtTime(p0):
    a = _ft['TimeMap_GetDividedBpmAtTime']
    f = CFUNCTYPE(c_double, c_double)(a)
    t = (c_double(p0),)
    r = f(t[0])
    return r


def RPR_TimeMap_GetTimeSigAtTime(p0, p1, p2, p3, p4):
    a = _ft['TimeMap_GetTimeSigAtTime']
    f = CFUNCTYPE(None, c_uint, c_double, c_void_p, c_void_p, c_void_p)(a)
    t = (rpr_packp('ReaProject*', p0), c_double(p1), c_int(p2), c_int(p3), c_double(p4))
    f(t[0], t[1], byref(t[2]), byref(t[3]), byref(t[4]))
    return (p0, p1, int(t[2].value), int(t[3].value), float(t[4].value))


def RPR_TimeMap_QNToTime(p0):
    a = _ft['TimeMap_QNToTime']
    f = CFUNCTYPE(c_double, c_double)(a)
    t = (c_double(p0),)
    r = f(t[0])
    return r


def RPR_TimeMap_timeToQN(p0):
    a = _ft['TimeMap_timeToQN']
    f = CFUNCTYPE(c_double, c_double)(a)
    t = (c_double(p0),)
    r = f(t[0])
    return r


def RPR_Track_GetPeakHoldDB(p0, p1, p2):
    a = _ft['Track_GetPeakHoldDB']
    f = CFUNCTYPE(c_double, c_uint, c_int, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_byte(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_Track_GetPeakInfo(p0, p1):
    a = _ft['Track_GetPeakInfo']
    f = CFUNCTYPE(c_double, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_TrackFX_FormatParamValue(p0, p1, p2, p3, p4, p5):
    a = _ft['TrackFX_FormatParamValue']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_int, c_double, c_char_p, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_int(p2), c_double(p3), rpr_packs(p4), c_int(p5))
    r = f(t[0], t[1], t[2], t[3], t[4], t[5])
    return (r, p0, p1, p2, p3, rpr_unpacks(t[4]), p5)


def RPR_TrackFX_FormatParamValueNormalized(p0, p1, p2, p3, p4, p5):
    a = _ft['TrackFX_FormatParamValueNormalized']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_int, c_double, c_char_p, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_int(p2), c_double(p3), rpr_packs(p4), c_int(p5))
    r = f(t[0], t[1], t[2], t[3], t[4], t[5])
    return (r, p0, p1, p2, p3, rpr_unpacks(t[4]), p5)


def RPR_TrackFX_GetChainVisible(p0):
    a = _ft['TrackFX_GetChainVisible']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return r


def RPR_TrackFX_GetCount(p0):
    a = _ft['TrackFX_GetCount']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return r


def RPR_TrackFX_GetEnabled(p0, p1):
    a = _ft['TrackFX_GetEnabled']
    f = CFUNCTYPE(c_byte, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_TrackFX_GetFloatingWindow(p0, p1):
    a = _ft['TrackFX_GetFloatingWindow']
    f = CFUNCTYPE(c_uint, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('HWND', r)


def RPR_TrackFX_GetFormattedParamValue(p0, p1, p2, p3, p4):
    a = _ft['TrackFX_GetFormattedParamValue']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_int, c_char_p, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_int(p2), rpr_packs(p3), c_int(p4))
    r = f(t[0], t[1], t[2], t[3], t[4])
    return (r, p0, p1, p2, rpr_unpacks(t[3]), p4)


def RPR_TrackFX_GetFXGUID(p0, p1):
    a = _ft['TrackFX_GetFXGUID']
    f = CFUNCTYPE(c_uint, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return rpr_unpackp('GUID*', r)


def RPR_TrackFX_GetFXName(p0, p1, p2, p3):
    a = _ft['TrackFX_GetFXName']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_char_p, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), rpr_packs(p2), c_int(p3))
    r = f(t[0], t[1], t[2], t[3])
    return (r, p0, p1, rpr_unpacks(t[2]), p3)


def RPR_TrackFX_GetInstrument(p0):
    a = _ft['TrackFX_GetInstrument']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('MediaTrack*', p0),)
    r = f(t[0])
    return r


def RPR_TrackFX_GetNumParams(p0, p1):
    a = _ft['TrackFX_GetNumParams']
    f = CFUNCTYPE(c_int, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_TrackFX_GetOpen(p0, p1):
    a = _ft['TrackFX_GetOpen']
    f = CFUNCTYPE(c_byte, c_uint, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1))
    r = f(t[0], t[1])
    return r


def RPR_TrackFX_GetParam(p0, p1, p2, p3, p4):
    a = _ft['TrackFX_GetParam']
    f = CFUNCTYPE(c_double, c_uint, c_int, c_int, c_void_p, c_void_p)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_int(p2), c_double(p3), c_double(p4))
    r = f(t[0], t[1], t[2], byref(t[3]), byref(t[4]))
    return (r, p0, p1, p2, float(t[3].value), float(t[4].value))


def RPR_TrackFX_GetParamName(p0, p1, p2, p3, p4):
    a = _ft['TrackFX_GetParamName']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_int, c_char_p, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_int(p2), rpr_packs(p3), c_int(p4))
    r = f(t[0], t[1], t[2], t[3], t[4])
    return (r, p0, p1, p2, rpr_unpacks(t[3]), p4)


def RPR_TrackFX_GetParamNormalized(p0, p1, p2):
    a = _ft['TrackFX_GetParamNormalized']
    f = CFUNCTYPE(c_double, c_uint, c_int, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_TrackFX_GetPreset(p0, p1, p2, p3):
    a = _ft['TrackFX_GetPreset']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_char_p, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), rpr_packs(p2), c_int(p3))
    r = f(t[0], t[1], t[2], t[3])
    return (r, p0, p1, rpr_unpacks(t[2]), p3)


def RPR_TrackFX_NavigatePresets(p0, p1, p2):
    a = _ft['TrackFX_NavigatePresets']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_int(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_TrackFX_SetEnabled(p0, p1, p2):
    a = _ft['TrackFX_SetEnabled']
    f = CFUNCTYPE(None, c_uint, c_int, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_byte(p2))
    f(t[0], t[1], t[2])


def RPR_TrackFX_SetOpen(p0, p1, p2):
    a = _ft['TrackFX_SetOpen']
    f = CFUNCTYPE(None, c_uint, c_int, c_byte)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_byte(p2))
    f(t[0], t[1], t[2])


def RPR_TrackFX_SetParam(p0, p1, p2, p3):
    a = _ft['TrackFX_SetParam']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_int, c_double)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_int(p2), c_double(p3))
    r = f(t[0], t[1], t[2], t[3])
    return r


def RPR_TrackFX_SetParamNormalized(p0, p1, p2, p3):
    a = _ft['TrackFX_SetParamNormalized']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_int, c_double)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_int(p2), c_double(p3))
    r = f(t[0], t[1], t[2], t[3])
    return r


def RPR_TrackFX_SetPreset(p0, p1, p2):
    a = _ft['TrackFX_SetPreset']
    f = CFUNCTYPE(c_byte, c_uint, c_int, c_char_p)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), rpr_packsc(p2))
    r = f(t[0], t[1], t[2])
    return r


def RPR_TrackFX_Show(p0, p1, p2):
    a = _ft['TrackFX_Show']
    f = CFUNCTYPE(None, c_uint, c_int, c_int)(a)
    t = (rpr_packp('MediaTrack*', p0), c_int(p1), c_int(p2))
    f(t[0], t[1], t[2])


def RPR_TrackList_AdjustWindows(p0):
    a = _ft['TrackList_AdjustWindows']
    f = CFUNCTYPE(None, c_byte)(a)
    t = (c_byte(p0),)
    f(t[0])


def RPR_TrackList_UpdateAllExternalSurfaces():
    a = _ft['TrackList_UpdateAllExternalSurfaces']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_Undo_BeginBlock():
    a = _ft['Undo_BeginBlock']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_Undo_BeginBlock2(p0):
    a = _ft['Undo_BeginBlock2']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('void*', p0),)
    f(t[0])


def RPR_Undo_CanRedo2(p0):
    a = _ft['Undo_CanRedo2']
    f = CFUNCTYPE(c_char_p, c_uint)(a)
    t = (rpr_packp('void*', p0),)
    r = f(t[0])
    return str(r.decode())


def RPR_Undo_CanUndo2(p0):
    a = _ft['Undo_CanUndo2']
    f = CFUNCTYPE(c_char_p, c_uint)(a)
    t = (rpr_packp('void*', p0),)
    r = f(t[0])
    return str(r.decode())


def RPR_Undo_DoRedo2(p0):
    a = _ft['Undo_DoRedo2']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('void*', p0),)
    r = f(t[0])
    return r


def RPR_Undo_DoUndo2(p0):
    a = _ft['Undo_DoUndo2']
    f = CFUNCTYPE(c_int, c_uint)(a)
    t = (rpr_packp('void*', p0),)
    r = f(t[0])
    return r


def RPR_Undo_EndBlock(p0, p1):
    a = _ft['Undo_EndBlock']
    f = CFUNCTYPE(None, c_char_p, c_int)(a)
    t = (rpr_packsc(p0), c_int(p1))
    f(t[0], t[1])


def RPR_Undo_EndBlock2(p0, p1, p2):
    a = _ft['Undo_EndBlock2']
    f = CFUNCTYPE(None, c_uint, c_char_p, c_int)(a)
    t = (rpr_packp('void*', p0), rpr_packsc(p1), c_int(p2))
    f(t[0], t[1], t[2])


def RPR_Undo_OnStateChange(p0):
    a = _ft['Undo_OnStateChange']
    f = CFUNCTYPE(None, c_char_p)(a)
    t = (rpr_packsc(p0),)
    f(t[0])


def RPR_Undo_OnStateChange2(p0, p1):
    a = _ft['Undo_OnStateChange2']
    f = CFUNCTYPE(None, c_uint, c_char_p)(a)
    t = (rpr_packp('void*', p0), rpr_packsc(p1))
    f(t[0], t[1])


def RPR_Undo_OnStateChange_Item(p0, p1, p2):
    a = _ft['Undo_OnStateChange_Item']
    f = CFUNCTYPE(None, c_uint, c_char_p, c_uint)(a)
    t = (rpr_packp('ReaProject*', p0), rpr_packsc(p1), rpr_packp('MediaItem*', p2))
    f(t[0], t[1], t[2])


def RPR_Undo_OnStateChangeEx(p0, p1, p2):
    a = _ft['Undo_OnStateChangeEx']
    f = CFUNCTYPE(None, c_char_p, c_int, c_int)(a)
    t = (rpr_packsc(p0), c_int(p1), c_int(p2))
    f(t[0], t[1], t[2])


def RPR_Undo_OnStateChangeEx2(p0, p1, p2, p3):
    a = _ft['Undo_OnStateChangeEx2']
    f = CFUNCTYPE(None, c_uint, c_char_p, c_int, c_int)(a)
    t = (rpr_packp('void*', p0), rpr_packsc(p1), c_int(p2), c_int(p3))
    f(t[0], t[1], t[2], t[3])


def RPR_UpdateArrange():
    a = _ft['UpdateArrange']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_UpdateItemInProject(p0):
    a = _ft['UpdateItemInProject']
    f = CFUNCTYPE(None, c_uint)(a)
    t = (rpr_packp('MediaItem*', p0),)
    f(t[0])


def RPR_UpdateTimeline():
    a = _ft['UpdateTimeline']
    f = CFUNCTYPE(None)(a)
    f()


def RPR_ViewPrefs(p0, p1):
    a = _ft['ViewPrefs']
    f = CFUNCTYPE(None, c_int, c_char_p)(a)
    t = (c_int(p0), rpr_packsc(p1))
    f(t[0], t[1])


def RPR_WDL_VirtualWnd_ScaledBlitBG(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
    a = _ft['WDL_VirtualWnd_ScaledBlitBG']
    f = CFUNCTYPE(c_byte, c_uint, c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_float, c_int)(a)
    t = (
    rpr_packp('LICE_IBitmap*', p0), rpr_packp('WDL_VirtualWnd_BGCfg*', p1), c_int(p2), c_int(p3), c_int(p4), c_int(p5),
    c_int(p6), c_int(p7), c_int(p8), c_int(p9), c_float(p10), c_int(p11))
    r = f(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11])
    return r

