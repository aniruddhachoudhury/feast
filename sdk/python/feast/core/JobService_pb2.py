# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/JobService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.specs import ImportSpec_pb2 as feast_dot_specs_dot_ImportSpec__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/core/JobService.proto',
  package='feast.core',
  syntax='proto3',
  serialized_options=_b('\n\nfeast.coreB\017JobServiceProtoZ5github.com/gojek/feast/protos/generated/go/feast/core'),
  serialized_pb=_b('\n\x1b\x66\x65\x61st/core/JobService.proto\x12\nfeast.core\x1a\x1c\x66\x65\x61st/specs/ImportSpec.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc9\x05\n\x0fJobServiceTypes\x1aS\n\x16SubmitImportJobRequest\x12+\n\nimportSpec\x18\x01 \x01(\x0b\x32\x17.feast.specs.ImportSpec\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a(\n\x17SubmitImportJobResponse\x12\r\n\x05jobId\x18\x01 \x01(\t\x1aG\n\x10ListJobsResponse\x12\x33\n\x04jobs\x18\x01 \x03(\x0b\x32%.feast.core.JobServiceTypes.JobDetail\x1a\x1b\n\rGetJobRequest\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x44\n\x0eGetJobResponse\x12\x32\n\x03job\x18\x01 \x01(\x0b\x32%.feast.core.JobServiceTypes.JobDetail\x1a\x1d\n\x0f\x41\x62ortJobRequest\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x1e\n\x10\x41\x62ortJobResponse\x12\n\n\x02id\x18\x01 \x01(\t\x1a\xcb\x02\n\tJobDetail\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65xtId\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0e\n\x06runner\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x10\n\x08\x65ntities\x18\x06 \x03(\t\x12\x10\n\x08\x66\x65\x61tures\x18\x07 \x03(\t\x12\x43\n\x07metrics\x18\x08 \x03(\x0b\x32\x32.feast.core.JobServiceTypes.JobDetail.MetricsEntry\x12/\n\x0blastUpdated\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07\x63reated\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a.\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x32\x9c\x03\n\nJobService\x12t\n\tSubmitJob\x12\x32.feast.core.JobServiceTypes.SubmitImportJobRequest\x1a\x33.feast.core.JobServiceTypes.SubmitImportJobResponse\x12P\n\x08ListJobs\x12\x16.google.protobuf.Empty\x1a,.feast.core.JobServiceTypes.ListJobsResponse\x12_\n\x06GetJob\x12).feast.core.JobServiceTypes.GetJobRequest\x1a*.feast.core.JobServiceTypes.GetJobResponse\x12\x65\n\x08\x41\x62ortJob\x12+.feast.core.JobServiceTypes.AbortJobRequest\x1a,.feast.core.JobServiceTypes.AbortJobResponseBT\n\nfeast.coreB\x0fJobServiceProtoZ5github.com/gojek/feast/protos/generated/go/feast/coreb\x06proto3')
  ,
  dependencies=[feast_dot_specs_dot_ImportSpec__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_JOBSERVICETYPES_SUBMITIMPORTJOBREQUEST = _descriptor.Descriptor(
  name='SubmitImportJobRequest',
  full_name='feast.core.JobServiceTypes.SubmitImportJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='importSpec', full_name='feast.core.JobServiceTypes.SubmitImportJobRequest.importSpec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.core.JobServiceTypes.SubmitImportJobRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=238,
)

_JOBSERVICETYPES_SUBMITIMPORTJOBRESPONSE = _descriptor.Descriptor(
  name='SubmitImportJobResponse',
  full_name='feast.core.JobServiceTypes.SubmitImportJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobId', full_name='feast.core.JobServiceTypes.SubmitImportJobResponse.jobId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=280,
)

_JOBSERVICETYPES_LISTJOBSRESPONSE = _descriptor.Descriptor(
  name='ListJobsResponse',
  full_name='feast.core.JobServiceTypes.ListJobsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobs', full_name='feast.core.JobServiceTypes.ListJobsResponse.jobs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=353,
)

_JOBSERVICETYPES_GETJOBREQUEST = _descriptor.Descriptor(
  name='GetJobRequest',
  full_name='feast.core.JobServiceTypes.GetJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='feast.core.JobServiceTypes.GetJobRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=382,
)

_JOBSERVICETYPES_GETJOBRESPONSE = _descriptor.Descriptor(
  name='GetJobResponse',
  full_name='feast.core.JobServiceTypes.GetJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='feast.core.JobServiceTypes.GetJobResponse.job', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=384,
  serialized_end=452,
)

_JOBSERVICETYPES_ABORTJOBREQUEST = _descriptor.Descriptor(
  name='AbortJobRequest',
  full_name='feast.core.JobServiceTypes.AbortJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='feast.core.JobServiceTypes.AbortJobRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=454,
  serialized_end=483,
)

_JOBSERVICETYPES_ABORTJOBRESPONSE = _descriptor.Descriptor(
  name='AbortJobResponse',
  full_name='feast.core.JobServiceTypes.AbortJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='feast.core.JobServiceTypes.AbortJobResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=485,
  serialized_end=515,
)

_JOBSERVICETYPES_JOBDETAIL_METRICSENTRY = _descriptor.Descriptor(
  name='MetricsEntry',
  full_name='feast.core.JobServiceTypes.JobDetail.MetricsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.core.JobServiceTypes.JobDetail.MetricsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.core.JobServiceTypes.JobDetail.MetricsEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=803,
  serialized_end=849,
)

_JOBSERVICETYPES_JOBDETAIL = _descriptor.Descriptor(
  name='JobDetail',
  full_name='feast.core.JobServiceTypes.JobDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='feast.core.JobServiceTypes.JobDetail.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extId', full_name='feast.core.JobServiceTypes.JobDetail.extId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='feast.core.JobServiceTypes.JobDetail.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runner', full_name='feast.core.JobServiceTypes.JobDetail.runner', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='feast.core.JobServiceTypes.JobDetail.status', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entities', full_name='feast.core.JobServiceTypes.JobDetail.entities', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='feast.core.JobServiceTypes.JobDetail.features', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='feast.core.JobServiceTypes.JobDetail.metrics', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastUpdated', full_name='feast.core.JobServiceTypes.JobDetail.lastUpdated', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='feast.core.JobServiceTypes.JobDetail.created', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_JOBSERVICETYPES_JOBDETAIL_METRICSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=518,
  serialized_end=849,
)

_JOBSERVICETYPES = _descriptor.Descriptor(
  name='JobServiceTypes',
  full_name='feast.core.JobServiceTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_JOBSERVICETYPES_SUBMITIMPORTJOBREQUEST, _JOBSERVICETYPES_SUBMITIMPORTJOBRESPONSE, _JOBSERVICETYPES_LISTJOBSRESPONSE, _JOBSERVICETYPES_GETJOBREQUEST, _JOBSERVICETYPES_GETJOBRESPONSE, _JOBSERVICETYPES_ABORTJOBREQUEST, _JOBSERVICETYPES_ABORTJOBRESPONSE, _JOBSERVICETYPES_JOBDETAIL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=849,
)

_JOBSERVICETYPES_SUBMITIMPORTJOBREQUEST.fields_by_name['importSpec'].message_type = feast_dot_specs_dot_ImportSpec__pb2._IMPORTSPEC
_JOBSERVICETYPES_SUBMITIMPORTJOBREQUEST.containing_type = _JOBSERVICETYPES
_JOBSERVICETYPES_SUBMITIMPORTJOBRESPONSE.containing_type = _JOBSERVICETYPES
_JOBSERVICETYPES_LISTJOBSRESPONSE.fields_by_name['jobs'].message_type = _JOBSERVICETYPES_JOBDETAIL
_JOBSERVICETYPES_LISTJOBSRESPONSE.containing_type = _JOBSERVICETYPES
_JOBSERVICETYPES_GETJOBREQUEST.containing_type = _JOBSERVICETYPES
_JOBSERVICETYPES_GETJOBRESPONSE.fields_by_name['job'].message_type = _JOBSERVICETYPES_JOBDETAIL
_JOBSERVICETYPES_GETJOBRESPONSE.containing_type = _JOBSERVICETYPES
_JOBSERVICETYPES_ABORTJOBREQUEST.containing_type = _JOBSERVICETYPES
_JOBSERVICETYPES_ABORTJOBRESPONSE.containing_type = _JOBSERVICETYPES
_JOBSERVICETYPES_JOBDETAIL_METRICSENTRY.containing_type = _JOBSERVICETYPES_JOBDETAIL
_JOBSERVICETYPES_JOBDETAIL.fields_by_name['metrics'].message_type = _JOBSERVICETYPES_JOBDETAIL_METRICSENTRY
_JOBSERVICETYPES_JOBDETAIL.fields_by_name['lastUpdated'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOBSERVICETYPES_JOBDETAIL.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOBSERVICETYPES_JOBDETAIL.containing_type = _JOBSERVICETYPES
DESCRIPTOR.message_types_by_name['JobServiceTypes'] = _JOBSERVICETYPES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobServiceTypes = _reflection.GeneratedProtocolMessageType('JobServiceTypes', (_message.Message,), dict(

  SubmitImportJobRequest = _reflection.GeneratedProtocolMessageType('SubmitImportJobRequest', (_message.Message,), dict(
    DESCRIPTOR = _JOBSERVICETYPES_SUBMITIMPORTJOBREQUEST,
    __module__ = 'feast.core.JobService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.JobServiceTypes.SubmitImportJobRequest)
    ))
  ,

  SubmitImportJobResponse = _reflection.GeneratedProtocolMessageType('SubmitImportJobResponse', (_message.Message,), dict(
    DESCRIPTOR = _JOBSERVICETYPES_SUBMITIMPORTJOBRESPONSE,
    __module__ = 'feast.core.JobService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.JobServiceTypes.SubmitImportJobResponse)
    ))
  ,

  ListJobsResponse = _reflection.GeneratedProtocolMessageType('ListJobsResponse', (_message.Message,), dict(
    DESCRIPTOR = _JOBSERVICETYPES_LISTJOBSRESPONSE,
    __module__ = 'feast.core.JobService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.JobServiceTypes.ListJobsResponse)
    ))
  ,

  GetJobRequest = _reflection.GeneratedProtocolMessageType('GetJobRequest', (_message.Message,), dict(
    DESCRIPTOR = _JOBSERVICETYPES_GETJOBREQUEST,
    __module__ = 'feast.core.JobService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.JobServiceTypes.GetJobRequest)
    ))
  ,

  GetJobResponse = _reflection.GeneratedProtocolMessageType('GetJobResponse', (_message.Message,), dict(
    DESCRIPTOR = _JOBSERVICETYPES_GETJOBRESPONSE,
    __module__ = 'feast.core.JobService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.JobServiceTypes.GetJobResponse)
    ))
  ,

  AbortJobRequest = _reflection.GeneratedProtocolMessageType('AbortJobRequest', (_message.Message,), dict(
    DESCRIPTOR = _JOBSERVICETYPES_ABORTJOBREQUEST,
    __module__ = 'feast.core.JobService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.JobServiceTypes.AbortJobRequest)
    ))
  ,

  AbortJobResponse = _reflection.GeneratedProtocolMessageType('AbortJobResponse', (_message.Message,), dict(
    DESCRIPTOR = _JOBSERVICETYPES_ABORTJOBRESPONSE,
    __module__ = 'feast.core.JobService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.JobServiceTypes.AbortJobResponse)
    ))
  ,

  JobDetail = _reflection.GeneratedProtocolMessageType('JobDetail', (_message.Message,), dict(

    MetricsEntry = _reflection.GeneratedProtocolMessageType('MetricsEntry', (_message.Message,), dict(
      DESCRIPTOR = _JOBSERVICETYPES_JOBDETAIL_METRICSENTRY,
      __module__ = 'feast.core.JobService_pb2'
      # @@protoc_insertion_point(class_scope:feast.core.JobServiceTypes.JobDetail.MetricsEntry)
      ))
    ,
    DESCRIPTOR = _JOBSERVICETYPES_JOBDETAIL,
    __module__ = 'feast.core.JobService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.JobServiceTypes.JobDetail)
    ))
  ,
  DESCRIPTOR = _JOBSERVICETYPES,
  __module__ = 'feast.core.JobService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.JobServiceTypes)
  ))
_sym_db.RegisterMessage(JobServiceTypes)
_sym_db.RegisterMessage(JobServiceTypes.SubmitImportJobRequest)
_sym_db.RegisterMessage(JobServiceTypes.SubmitImportJobResponse)
_sym_db.RegisterMessage(JobServiceTypes.ListJobsResponse)
_sym_db.RegisterMessage(JobServiceTypes.GetJobRequest)
_sym_db.RegisterMessage(JobServiceTypes.GetJobResponse)
_sym_db.RegisterMessage(JobServiceTypes.AbortJobRequest)
_sym_db.RegisterMessage(JobServiceTypes.AbortJobResponse)
_sym_db.RegisterMessage(JobServiceTypes.JobDetail)
_sym_db.RegisterMessage(JobServiceTypes.JobDetail.MetricsEntry)


DESCRIPTOR._options = None
_JOBSERVICETYPES_JOBDETAIL_METRICSENTRY._options = None

_JOBSERVICE = _descriptor.ServiceDescriptor(
  name='JobService',
  full_name='feast.core.JobService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=852,
  serialized_end=1264,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubmitJob',
    full_name='feast.core.JobService.SubmitJob',
    index=0,
    containing_service=None,
    input_type=_JOBSERVICETYPES_SUBMITIMPORTJOBREQUEST,
    output_type=_JOBSERVICETYPES_SUBMITIMPORTJOBRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListJobs',
    full_name='feast.core.JobService.ListJobs',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_JOBSERVICETYPES_LISTJOBSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetJob',
    full_name='feast.core.JobService.GetJob',
    index=2,
    containing_service=None,
    input_type=_JOBSERVICETYPES_GETJOBREQUEST,
    output_type=_JOBSERVICETYPES_GETJOBRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AbortJob',
    full_name='feast.core.JobService.AbortJob',
    index=3,
    containing_service=None,
    input_type=_JOBSERVICETYPES_ABORTJOBREQUEST,
    output_type=_JOBSERVICETYPES_ABORTJOBRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_JOBSERVICE)

DESCRIPTOR.services_by_name['JobService'] = _JOBSERVICE

# @@protoc_insertion_point(module_scope)
