// Code generated by the FlatBuffers compiler. DO NOT EDIT.

package gamma_api

import (
	flatbuffers "github.com/google/flatbuffers/go"
)

type CacheInfo struct {
	_tab flatbuffers.Table
}

func GetRootAsCacheInfo(buf []byte, offset flatbuffers.UOffsetT) *CacheInfo {
	n := flatbuffers.GetUOffsetT(buf[offset:])
	x := &CacheInfo{}
	x.Init(buf, n+offset)
	return x
}

func GetSizePrefixedRootAsCacheInfo(buf []byte, offset flatbuffers.UOffsetT) *CacheInfo {
	n := flatbuffers.GetUOffsetT(buf[offset+flatbuffers.SizeUint32:])
	x := &CacheInfo{}
	x.Init(buf, n+offset+flatbuffers.SizeUint32)
	return x
}

func (rcv *CacheInfo) Init(buf []byte, i flatbuffers.UOffsetT) {
	rcv._tab.Bytes = buf
	rcv._tab.Pos = i
}

func (rcv *CacheInfo) Table() flatbuffers.Table {
	return rcv._tab
}

func (rcv *CacheInfo) FieldName() []byte {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(4))
	if o != 0 {
		return rcv._tab.ByteVector(o + rcv._tab.Pos)
	}
	return nil
}

func (rcv *CacheInfo) CacheSize() int32 {
	o := flatbuffers.UOffsetT(rcv._tab.Offset(6))
	if o != 0 {
		return rcv._tab.GetInt32(o + rcv._tab.Pos)
	}
	return 0
}

func (rcv *CacheInfo) MutateCacheSize(n int32) bool {
	return rcv._tab.MutateInt32Slot(6, n)
}

func CacheInfoStart(builder *flatbuffers.Builder) {
	builder.StartObject(2)
}
func CacheInfoAddFieldName(builder *flatbuffers.Builder, fieldName flatbuffers.UOffsetT) {
	builder.PrependUOffsetTSlot(0, flatbuffers.UOffsetT(fieldName), 0)
}
func CacheInfoAddCacheSize(builder *flatbuffers.Builder, cacheSize int32) {
	builder.PrependInt32Slot(1, cacheSize, 0)
}
func CacheInfoEnd(builder *flatbuffers.Builder) flatbuffers.UOffsetT {
	return builder.EndObject()
}