package autoregister

import (
	"context"
	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	//balanceservice.BalanceService
	balanceservicepb "github.com/maltenorstroem/tbb-api-spec/balanceservice"

	"google.golang.org/grpc"
)

func RegisterAllEndpoints(grpcBackendAddr string, ctx context.Context, mux *runtime.ServeMux, opts []grpc.DialOption) error {
	var err error
	// balanceservice.BalanceService
	err = balanceservicepb.RegisterBalanceServiceHandlerFromEndpoint(ctx, mux, grpcBackendAddr, opts)
	if err != nil {
		return err
	}

	//installed services
	return err
}
