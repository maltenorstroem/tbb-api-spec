name: ListBalancesRequest
type: ListBalancesRequest
description: request message for ListBalances
lifecycle: null
__proto:
    package: balanceservice
    targetfile: reqmsgs.proto
    imports:
        - google/protobuf/empty.proto
    options:
        go_package: github.com/maltenorstroem/tbb-api-spec/balanceservice;balanceservicepb
        java_multiple_files: "true"
        java_outer_classname: ReqmsgsProto
        java_package: com.github.maltenorstroem.tbb.api.balanceservice
fields:
    body:
        type: .google.protobuf.Empty
        description: Body with google.protobuf.Empty
        __proto:
            number: 1
        __ui: null
        meta:
            default: ""
            placeholder: balanceservice.listbalancesrequest.body.placeholder
            hint: ""
            label: balanceservice.listbalancesrequest.body.label
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
